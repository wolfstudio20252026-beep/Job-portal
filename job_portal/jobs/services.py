import requests

JOOBLE_API_KEY = "31579ff5-cbc1-4937-9968-a2f707af7bef"

def search_jobs(keywords="", location=""):
    url = f"https://jooble.org/api/{JOOBLE_API_KEY}"

    payload = {
        "keywords": keywords,
        "location": location,
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json()

    return None