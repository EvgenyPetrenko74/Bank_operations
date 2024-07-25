import os

import requests
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


def all_amount_rub_convert(transaction: dict):
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]
        if currency == "RUB":
            return amount
        else:
            if currency != "RUB":
                url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
                response = requests.request("GET", url, headers={"apikey": api_key})
                data = response.json()
                return data["result"]
    except (KeyError, TypeError, ValueError, requests.RequestException) as e:
        print(f"Error: {e}")
        return 0.0


transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560",
}
empty_dict = {}

res = all_amount_rub_convert(transaction)
print(res)
