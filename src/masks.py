def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    if len(card_number) == 16 and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    elif len(card_number) == 0:
        return " Номер отсутствует"
    else:
        return " Длина номера не верная или введены посторонние символы"

def funk():
    pass

def jhv():
    pass

def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счёта"""
    if len(account_number) == 20 and account_number.isdigit():
        mask_account_number = "** " + account_number[-4:]
        return mask_account_number
    elif len(account_number) == 0:
        return " Номер отсутствует"
    else:
        return " Длина номера не верная или введены посторонние символы"


if __name__ == "__main__":
    print(get_mask_card_number(str(1111222233334444)))
    print(get_mask_account(str(11112222333344445555)))
