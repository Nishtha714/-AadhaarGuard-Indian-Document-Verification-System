from deepface import DeepFace
import cv2
import numpy as np
import tempfile

def extract_face(image_bytes):
    np_arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return None

    x, y, w, h = faces[0]
    face = img[y:y+h, x:x+w]

    return face


def compare_faces(aadhaar_bytes, selfie_bytes):
    try:
        # Extract face from Aadhaar
        aadhaar_face = extract_face(aadhaar_bytes)

        if aadhaar_face is None:
            return 0.0, 1.0

        # Decode selfie
        np_arr = np.frombuffer(selfie_bytes, np.uint8)
        selfie_img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Save temp images
        temp1 = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        temp2 = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")

        cv2.imwrite(temp1.name, aadhaar_face)
        cv2.imwrite(temp2.name, selfie_img)

        # DeepFace comparison
        result = DeepFace.verify(
            temp1.name,
            temp2.name,
            model_name="Facenet",
            enforce_detection=False
        )

        similarity = 1 - result["distance"]

        return float(similarity), float(result["distance"])

    except Exception as e:
        print("Error:", e)
        return 0.0, 1.0