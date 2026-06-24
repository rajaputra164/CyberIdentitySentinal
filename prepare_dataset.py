import pandas as pd

df = pd.read_csv("datasets/profiles.csv")

df["label"] = df["label"].map({
    "real": 0,
    "fake": 1
})

print(df["label"].value_counts())

df.to_csv("datasets/profiles_clean.csv", index=False)

print("Dataset saved as profiles_clean.csv")