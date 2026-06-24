def explain_risk(risk, bot_score):

    if risk == "High":
        return (
            "The account appears suspicious because "
            "its profile metrics indicate a high likelihood "
            "of being fake or automated."
        )

    if bot_score > 70:
        return (
            "The account shows bot-like behavior including "
            "abnormal activity patterns."
        )

    return "The account shows relatively normal behavior."