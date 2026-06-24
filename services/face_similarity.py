from deepface import DeepFace


def compare_faces(img1, img2):
    result = DeepFace.verify(img1, img2)

    score = round((1 - result["distance"]) * 100)

    return {
        "match": result["verified"],
        "score": score
    }