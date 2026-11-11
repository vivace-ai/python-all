# 학습 기록 프로그램 19단계: 내가 만든 서비스에 연결한다
import os

import requests

from study_log.log import StudyLog
from study_log.report import summary_table
from study_log.storage_remote import RemoteStorage

SERVER = "http://127.0.0.1:8025"
KEY = os.environ.get("STUDY_API_KEY", "demo-key")

log = StudyLog(RemoteStorage(SERVER))   # 21장의 보관소 그대로다
print(f"서버에 기록 {len(log)}건이 있습니다.")

log.add("파이썬", 1.5)
log.add("영어", 1.0)
log.add("파이썬", 2.0, score=90)
print(summary_table(log))

headers = {"Authorization": f"Bearer {KEY}"}
response = requests.get(f"{SERVER}/advice", headers=headers, timeout=30)
response.raise_for_status()
print(response.json()["advice"])
