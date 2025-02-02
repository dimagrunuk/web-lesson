import requests

API_URL = "https://habit-tracker-back-pt2-c5de98999abd.herokuapp.com"

def register(email, password, name):
    data = {
        "email": email,
        "password": password,
        "name": name
    }
    print(f"Відправка POST-запиту на {API_URL}/register з даними: {data}")
    try:
        response = requests.post(f"{API_URL}/register", json=data)
        response.raise_for_status()  # Викидає помилку при статусах 4xx/5xx
        print(f"Відповідь сервера: {response.status_code} {response.text}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Помилка запиту: {e}")
        return {"message": "Помилка підключення до сервера"}

def login(email, password):
    data = {
        "email": email,
        "password": password
    }
    print(f"Відправка POST-запиту на {API_URL}/login з даними: {data}")
    try:
        response = requests.post(f"{API_URL}/login", json=data)
        response.raise_for_status()  # Викидає помилку при статусах 4xx/5xx
        print(f"Відповідь сервера: {response.status_code} {response.text}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Помилка при логіні: {e}")
        return {"message": "Помилка підключення до сервера"}
def add_habit(name, frequency):
    data = {
        "name": name,
        "frequency": frequency
    }
    print(f"Відправка POST-запиту на {API_URL}/habit з даними: {data}")
    try:
        response = requests.post(f"{API_URL}/habit", json=data)
        response.raise_for_status()  # Викидає помилку при статусах 4xx/5xx
        print(f"Відповідь сервера: {response.status_code} {response.text}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Помилка при додаванні звички: {e}")
        return {"message": "Помилка підключення до сервера"}
