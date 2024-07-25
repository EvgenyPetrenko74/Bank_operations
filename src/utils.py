import json


def get_info(file_json: str):
    try:
        with open(file_json, encoding="utf-8") as f:
            trans = json.load(f)
            return trans
    except FileNotFoundError as e:
        return f"Error: {e}"


result = get_info("../data/operations.json")
print(result)
