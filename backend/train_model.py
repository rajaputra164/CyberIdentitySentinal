import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load cleaned dataset
df = pd.read_csv("datasets/profiles.csv")

# Create ratio feature if not already present
df["ratio"] = df["followers_count"] / (df["following_count"] + 1)

# Features
X = df[
    [
        "followers_count",
        "following_count",
        "posts_count",
        "account_age_days",
        "ratio"
    ]
]

# Target
y = df["label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy:.2f}")

# Save model
joblib.dump(model, "fake_model.pkl")

print("Model saved as fake_model.pkl")