from services.ai_copilot import explain_risk

result = explain_risk(
    risk="High",
    bot_score=78
)

print(result)