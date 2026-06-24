from services.behavior_analysis import analyze_behavior

result = analyze_behavior(
    posts_per_day=100,
    followers=10,
    following=5000,
    repeated_percent=80
)

print(result)