from app.feature_utils import hashed_feature

def predict(payload: dict) -> dict:
    user_id = payload.get("user_id", "")
    bucket = hashed_feature(str(user_id))
    return {"prediction": float(bucket) / 1024.0}
