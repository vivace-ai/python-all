from abc import ABC, abstractmethod


class Exporter(ABC):
    @abstractmethod
    def render(self, rows):
        """행의 리스트를 문자열로 바꾼다."""


class JsonExporter(Exporter):
    def rendor(self, rows):     # 이름의 철자가 틀렸다
        return str(rows)


exporter = JsonExporter()
