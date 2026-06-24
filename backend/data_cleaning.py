import pandas as pd

df = pd.read_csv("datasets/profiles.csv")

# Remove missing values
df = df.dropna()

# Remove duplicate rows
df = df.drop_duplicates()

# Create follower/following ratio feature
df["ratio"] = df["followers_count"] / (df["following_count"] + 1)

print(df.head())

# Optional: save cleaned dataset
df.to_csv("datasets/profiles_clean.csv", index=False)

print("Data cleaning completed!")