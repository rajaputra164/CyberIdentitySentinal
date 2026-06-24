from rapidfuzz import fuzz

def username_similarity(username1, username2):
    return round(
        fuzz.ratio(username1.lower(), username2.lower()),
        2
    )

print(
    username_similarity(
        "john_doe",
        "john.doe"
    )
)