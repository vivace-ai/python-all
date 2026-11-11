from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()
BOOKS = {1: "파이썬 완전 정복", 2: "처음 만나는 통계"}


@app.get("/books/{number}")
def get_book(number: int) -> dict:
    if number not in BOOKS:
        raise HTTPException(status_code=404, detail="그런 책이 없습니다.")
    return {"number": number, "title": BOOKS[number]}


client = TestClient(app)
for path in ["/books/1", "/books/9", "/books/첫째"]:
    response = client.get(path)
    print(path, "->", response.status_code)
