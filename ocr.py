import pytesseract
import cv2
import numpy as np
import re


def preprocess_image(file_bytes):
    np_arr = np.frombuffer(file_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray


def extract_text(file_bytes):
    img = preprocess_image(file_bytes)
    text = pytesseract.image_to_string(img)
    return text


def extract_aadhaar_details(text):

    # Aadhaar number
    aadhaar = re.findall(r'\d{4}\s\d{4}\s\d{4}', text)
    aadhaar = aadhaar[0] if aadhaar else None

    # DOB
    dob = re.findall(r'\d{2}/\d{2}/\d{4}', text)
    dob = dob[0] if dob else None

    # Name (basic logic)
    lines = text.split("\n")
    name = None

    for line in lines:
        line = line.strip()
        if len(line) > 3 and line.replace(" ", "").isalpha():
            name = line
            break

    return {
        "Name": name,
        "DOB": dob,
        "Aadhaar": aadhaar
    }