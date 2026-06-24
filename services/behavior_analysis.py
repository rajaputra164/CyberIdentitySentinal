def analyze_behavior(posts_per_day, followers, following, repeated_percent):

    bot_score = 0

    # Posting frequency
    if posts_per_day > 50:
        bot_score += 40

    # Followers ratio
    ratio = followers / (following + 1)

    if ratio < 0.1:
        bot_score += 30

    # Repeated content
    if repeated_percent > 50:
        bot_score += 30

    return {
        "bot_score": bot_score
    }