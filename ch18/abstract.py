from abc import ABC, abstractmethod


class Exporter(ABC):
    """기록을 내보내는 방식의 공통 틀."""

    @abstractmethod
    def render(self, rows):
        """행의 리스트를 문자열로 바꾼다. 자식이 반드시 정의한다."""

    def export(self, rows):
        return f"{self.render(rows)}\n({len(rows)}건)"


class CsvExporter(Exporter):
    def render(self, rows):
        return "\n".join(f"{name},{hours}" for name, hours in rows)


class MarkdownExporter(Exporter):
    def render(self, rows):
        return "\n".join(f"| {name} | {hours} |" for name, hours in rows)


rows = [("파이썬", 3.5), ("통계학", 2.0)]
for exporter in (CsvExporter(), MarkdownExporter()):
    print(exporter.export(rows))
