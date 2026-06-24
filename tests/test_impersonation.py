from services.impersonation_detector import calculate_impersonation

result = calculate_impersonation(
    username_score=87.5,
    face_score=91
)

print(result)