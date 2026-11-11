from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/bmi")
def bmi(height: float, weight: float) -> dict:
    """키(cm)와 몸무게(kg)로 체질량지수를 구한다."""
    value = weight / (height / 100) ** 2
    return {"bmi": round(value, 1)}


client = TestClient(app)
print(client.get("/bmi?height=170&weight=65").json())
print(client.get("/bmi?height=170").status_code)
