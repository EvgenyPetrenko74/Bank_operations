
def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    if len(card_number) == 16 and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    elif len(card_number) == 0:
        return "Строка пустая"
    elif card_number.isdigit() == False:
        return "Введены посторонние символы"
    else:
        return "Длина номера не верная"

def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счёта"""
    if len(account_number) == 20 and account_number.isdigit():
        mask_account_number = "** " + account_number[-4:]
        return mask_account_number
    elif len(account_number) == 0:
        return "Строка пустая"
    elif account_number.isdigit() == False:
        return "Введены посторонние символы"
    else:
        return "Длина номера не верная"

if __name__ == "__main__":
    print(get_mask_card_number(str(1111222233334444)))
    print(get_mask_account(str(6757463)))
