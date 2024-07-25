import random
import requests
import json
import os
from dotenv import load_dotenv


def generate_users(first_name: list[str], last_name: list[str], city: list[str]):
    """Генерирует пользователя."""

    while True:
        user = {
            "first_name": random.choice(first_name),
            "last_name": random.choice(last_name),
            "age": random.randint(18, 65),
            "city": random.choice(city),
        }
        yield user


if __name__ == "__main__":
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia"]
    first_names = ["John", "Jane", "Mark", "Emily", "Michael", "Sarah"]
    last_names = ["Doe", "Smith", "Johnson", "Brown", "Lee", "Wilson"]

    users = generate_users(first_names, last_names, cities)

    user_group1 = [next(users) for i in range(4)]
    user_group2 = [next(users) for i in range(6)]

    # print('User group #1')
    # print(json.dumps(user_group1, indent=4))
    # print('User group #2')
    # print(json.dumps(user_group2, indent=4))

# Загрузка переменных из .env-файла
load_dotenv()

# Получение значения переменной GITHUB_TOKEN из .env-файла
github_token = os.getenv("API_KEY")

# Создание заголовка с токеном доступа API
headers = {"Authorization": f"token {github_token}"}

# Отправка GET-запроса к API
response = requests.get("https://api.github.com/user", headers=headers)

# Обработка ответа
print(response.json())
