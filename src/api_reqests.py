import requests
import json

# r = requests.get('https://imgs.xkcd.com/comics/python.png')
# print(r.content)
# with open('comic.png', 'wb') as f:
#     f.write(r.content)


def get_github_users(users):
    results = []
    for user in users:
        status, user_data = get_user_info(user)
        if not status:
            continue

        status, repositories = get_user_repos(user)
        if not status:
            continue

        result = {"login": user_data["login"], "public_repos": user_data["public_repos"], "repositories": repositories}
        results.append(result)
    return json.dumps(results)


def get_user_info(user: str) -> tuple[bool, dict]:
    url = f"https://api.github.com/users/{user}"
    response = requests.get(url)
    if response.status_code != 200:
        return False, {}
    return True, response.json()


def get_user_repos(user: str) -> tuple[bool, list]:
    repo_url = f"https://api.github.com/users/{user}/repos"
    repo_response = requests.get(repo_url)
    if repo_response.status_code != 200:
        return False, []
    return True, [repo["name"] for repo in repo_response.json()]


def get_currency_rate(date, currency_code):
    url = f"https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to get currency rate for date {date}")
    data = response.json()
    currency_data = data["Valute"].get(currency_code)
    if not currency_data:
        raise ValueError(f"No data for currency {currency_code}")
    return {
        "date": date,
        "currency_code": currency_code,
        "rate": currency_data["Value"],
    }


rate = get_currency_rate("2024-07-25", "USD")
print(rate)

# userinfo = get_user_info('EvgenyPetrenko74')
# print(userinfo)

# usrrrepos = get_user_repos('EvgenyPetrenko74')
# print(usrrrepos)

# result = get_github_users(['EvgenyPetrenko74'])
# print(result)
