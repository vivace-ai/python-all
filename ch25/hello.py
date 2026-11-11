from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello(name: str = "파이썬") -> dict:
    return {"message": f"안녕하세요, {name}"}


@app.get("/double")
def double(n: int) -> dict:
    return {"n": n, "result": n * 2}
