from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load model
model = joblib.load("backend/fake_model.pkl")

# Input schema
class UserInput(BaseModel):
    followers: int
    following: int
    posts: int
    age: int


@app.post("/analyze")
def analyze(data: UserInput):

    ratio = data.followers / (data.following + 1)

    sample = pd.DataFrame([{
        "followers_count": data.followers,
        "following_count": data.following,
        "posts_count": data.posts,
        "account_age_days": data.age,
        "ratio": ratio
    }])

    # predict fake probability (class 0 = fake as per your fix)
    fake_prob = model.predict_proba(sample)[0][0]

    score = round(fake_prob * 100)

    if score > 80:
        risk = "High"
    elif score > 50:
        risk = "Medium"
    else:
        risk = "Low"

    return {
        "risk": risk,
        "score": score
    }