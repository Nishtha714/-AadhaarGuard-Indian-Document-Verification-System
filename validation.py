from datetime import datetime
import re

def validate_aadhaar(number):
    if number is None:
        return False
    return bool(re.match(r"\d{4}\s\d{4}\s\d{4}", number))


def calculate_age(dob):
    if dob is None:
        return None

    try:
        birth = datetime.strptime(dob, "%d/%m/%Y")
        today = datetime.today()

        age = today.year - birth.year - (
            (today.month, today.day) < (birth.month, birth.day)
        )
        return age
    except:
        return None