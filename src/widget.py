from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(string: str) -> str:
    """Функция маскирует номер карты или счета."""
    card_varieties = ["Maestro", "MasterCard", "Visa", "Счет"]
    find = -1
    for elem in card_varieties:
        if string.find(elem) != -1:
            find = elem
            break
    if find == "Счет":
        account = get_mask_account(string[-20:])
        mask_account = string.replace(string[-20:], account)
        return mask_account
    elif find != -1:
        card_number = get_mask_card_number(string[-16:])
        mask_card_number = string.replace(string[-16:], card_number)
        return mask_card_number
    else:
        return "Данные отсутствуют или введены неверно"


def get_data(data: str) -> str:
    """Функция, которая возвращает строку с датой в требуемом формате."""
    d = datetime.strptime(data, format("%Y-%m-%dt%H:%M:%S.%f"))
    return d.strftime("%d.%m.%Y")


if __name__ == "__main__":
    print(mask_account_card("Maestro 1111222233334444"))
    print(mask_account_card("Счет 11112222333344445555"))
    print(get_data("2018-07-11T02:26:18.671407"))
