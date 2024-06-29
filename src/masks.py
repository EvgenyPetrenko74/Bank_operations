
def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счёта"""
    mask_account_number = "*" * 2 + account_number[-4:]
    return mask_account_number


if __name__ == "__main__":
    print(get_mask_card_number(str(1111222233334444)))
    print(get_mask_account(str(11112222333344445555)))
