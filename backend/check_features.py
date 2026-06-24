import pandas as pd
import joblib

model = joblib.load("fake_model.pkl")

features = [
    "followers_count",
    "following_count",
    "posts_count",
    "account_age_days",
    "ratio"
]

for name, importance in zip(features, model.feature_importances_):
    print(f"{name}: {importance:.4f}")