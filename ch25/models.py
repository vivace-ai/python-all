"""서비스가 주고받는 데이터의 모양."""
from pydantic import BaseModel, Field


class RecordIn(BaseModel):
    """클라이언트가 보내는 기록."""

    subject: str = Field(min_length=1)
    hours: float = Field(gt=0, le=24)
    score: int | None = Field(default=None, ge=0, le=100)


class RecordOut(RecordIn):
    """서버가 돌려주는 기록. 일차 번호가 붙는다."""

    day: int


class Advice(BaseModel):
    advice: str
