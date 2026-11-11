from pydantic import BaseModel, Field


class RecordIn(BaseModel):
    subject: str = Field(min_length=1)
    hours: float = Field(gt=0, le=24)


RecordIn(subject="파이썬", hours=30)
