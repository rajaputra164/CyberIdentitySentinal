import pandas as pd
import joblib

# Load model
model = joblib.load("fake_model.pkl")
print(model.classes_)
sample_profile = pd.DataFrame([{
    "followers_count": 5,
    "following_count": 10000,
    "posts_count": 1,
    "account_age_days": 2,
    "ratio": 5 / (10000 + 1)
}])
# correct fake probability (based on class index 0)
probability_fake = model.predict_proba(sample_profile)[0][0]

score = round(probability_fake * 100)

if score > 80:
    risk = "High"
elif score > 50:
    risk = "Medium"
else:
    risk = "Low"

result = {
    "risk": risk,
    "score": score
}

print("Fake Probability:", probability_fake)
print(result)