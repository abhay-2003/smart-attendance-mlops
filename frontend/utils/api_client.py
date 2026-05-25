import requests


BASE_API_URL = "http://127.0.0.1:8000"


def check_api_health():

    response = requests.get(
        f"{BASE_API_URL}/"
    )

    return response.json()


def recognize_face(image_file):

    files = {
        "file": image_file
    }

    response = requests.post(
        f"{BASE_API_URL}/recognize",
        files=files
    )

    return response.json()


def fetch_attendance():

    response = requests.get(
        f"{BASE_API_URL}/attendance"
    )

    return response.json()