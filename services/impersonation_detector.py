def calculate_impersonation(username_score, face_score):

    final_score = round(
        (username_score * 0.4) +
        (face_score * 0.6)
    )

    if final_score >= 80:
        risk = "High"
    elif final_score >= 50:
        risk = "Medium"
    else:
        risk = "Low"

    return {
        "impersonation_probability": final_score,
        "risk": risk
    }