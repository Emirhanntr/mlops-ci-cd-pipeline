from fastapi import FastAPI
from app.model import predict


app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict_endpoint(payload: dict):
    return predict(payload)
