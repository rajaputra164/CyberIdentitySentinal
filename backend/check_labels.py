import pandas as pd

df = pd.read_csv("datasets/profiles.csv")

print(df["label"].value_counts())

print("\nFake Accounts:")
print(df[df["label"] == 1][[
    "followers_count",
    "following_count",
    "posts_count",
    "account_age_days"
]].describe())

print("\nReal Accounts:")
print(df[df["label"] == 0][[
    "followers_count",
    "following_count",
    "posts_count",
    "account_age_days"
]].describe())