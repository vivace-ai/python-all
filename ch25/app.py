"""학습 기록 서비스."""
import logging
import os
from collections.abc import Callable
from contextlib import closing
from pathlib import Path

import openai
from fastapi import Depends, FastAPI, Header, HTTPException

from llm import ask
from models import Advice, RecordIn, RecordOut
from study_log.coach import Coach
from study_log.log import StudyLog
from study_log.storage_sqlite import SqliteStorage

HERE = Path(__file__).parent
DB_FILE = Path(os.environ.get("STUDY_DB") or HERE / "study_log.db")
SERVICE_KEY = os.environ.get("STUDY_API_KEY", "demo-key")

logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("study")
logger.setLevel(logging.INFO)
app = FastAPI(title="학습 기록 서비스")


def get_ask() -> Callable[[list[dict]], str]:
    """모델을 부르는 함수를 내준다. 확인할 때는 가짜로 바꿔 끼운다."""
    return ask


def require_key(authorization: str | None = Header(default=None)) -> None:
    """키를 가진 요청만 통과시킨다."""
    if authorization != f"Bearer {SERVICE_KEY}":
        detail = "API 키가 없거나 틀렸습니다."
        raise HTTPException(status_code=401, detail=detail)


@app.get("/records")
def list_records() -> list[RecordOut]:
    with closing(SqliteStorage(DB_FILE)) as storage:
        log = StudyLog(storage)
        return [RecordOut.model_validate(r.to_dict()) for r in log.records]


@app.post("/records", status_code=201)
def add_record(body: RecordIn) -> RecordOut:
    with closing(SqliteStorage(DB_FILE)) as storage:
        log = StudyLog(storage)
        record = log.add(body.subject, body.hours, body.score)
    logger.info("기록 추가: %s", record)
    return RecordOut.model_validate(record.to_dict())


@app.get("/summary")
def summary() -> dict[str, float]:
    with closing(SqliteStorage(DB_FILE)) as storage:
        return StudyLog(storage).total_by_subject()


@app.get("/advice", dependencies=[Depends(require_key)])
def advice(ask_model: Callable = Depends(get_ask)) -> Advice:
    with closing(SqliteStorage(DB_FILE)) as storage:
        log = StudyLog(storage)
    if len(log) == 0:
        raise HTTPException(status_code=404, detail="기록이 아직 없습니다.")
    try:
        text = Coach(ask_model).advise(log)
    except openai.APIError as e:
        logger.warning("모델 호출 실패: %s", e)
        detail = "모델 서비스에 문제가 있습니다."
        raise HTTPException(status_code=502, detail=detail) from e
    return Advice(advice=text)
