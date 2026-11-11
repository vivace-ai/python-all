from pydantic import BaseModel, Field, ValidationError


class Signup(BaseModel):
    name: str = Field(min_length=2, max_length=20)
    age: int = Field(ge=14, le=120)
    email: str = Field(pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


forms = [
    {"name": "김서연", "age": "29", "email": "seoyeon@example.com"},
    {"name": "김", "age": 29, "email": "seoyeon@example.com"},
    {"name": "박준호", "age": 9, "email": "주소 아님"},
]
for form in forms:
    try:
        print("가입:", Signup(**form))
    except ValidationError as e:
        fields = [error["loc"][0] for error in e.errors()]
        print("거절:", fields)
