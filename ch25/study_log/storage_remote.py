"""기록을 웹 API 너머의 서버에 보관한다."""
import requests

from .records import StudyRecord, record_from_dict


class RemoteStorage:
    def __init__(self, base_url: str, timeout: float = 5) -> None:
        self.url = f"{base_url}/records"
        self.timeout = timeout

    def load(self) -> list[StudyRecord]:
        response = requests.get(self.url, timeout=self.timeout)
        response.raise_for_status()
        return [record_from_dict(item) for item in response.json()]

    def append(self, record: StudyRecord) -> None:
        response = requests.post(
            self.url, json=record.to_dict(), timeout=self.timeout
        )
        response.raise_for_status()
