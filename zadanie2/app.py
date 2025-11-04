# Damian Sadowski

import re
from datetime import datetime

def is_valid_email(email):
    # Dla pełnego (bezpiecznego) testu – użyj wyrażenia regularnego
    if not isinstance(email, str) or len(email) == 0:
        return False
    return re.match(r"^[^@]+@[^@]+\.[^@]+$", email) is not None

def rectangle_area(width, height):
    # Ujemne wartości traktowane jako 0
    if width < 0 or height < 0:
        return 0
    return width * height

def filter_positive(numbers):
    # Przyjmujemy tylko iterowalne liczby – lista może być pusta
    return [x for x in numbers if x > 0]

def parse_date(date_str):
    # Akceptowany wyłącznie format dd-mm-yyyy, inne rzucają błąd
    if not isinstance(date_str, str) or date_str == "":
        raise ValueError("Niepoprawny format daty")
    return datetime.strptime(date_str, "%d-%m-%Y").date()

def is_palindrome(text):
    # Akceptujemy każdy ciąg (również pusty) jako potencjalny palindrom
    if not isinstance(text, str):
        return False
    return text == text[::-1]

