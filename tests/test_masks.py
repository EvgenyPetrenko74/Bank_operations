from src.masks import get_mask_card_number, get_mask_account
import pytest

@pytest.mark.parametrize("card_number, masked_card_number", [
    ("card_number_f", "1111 22** **** 4444"),
    ("", "Строка пустая"),
    ("jgcj", "Введены посторонние символы"),
    ("6576554433", "Длина номера не верная"),
])
def test_get_mask_card_number(card_number, masked_card_number):
    assert get_mask_card_number(card_number) == masked_card_number

@pytest.mark.parametrize("account_number, masked_account_number", [
    ("account_number_f", "** 5555"),
    ("", "Строка пустая"),
    ("jgcj", "Введены посторонние символы"),
    ("6576554433", "Длина номера не верная"),
])
def test_get_mask_account(account_number, masked_account_number):
    assert get_mask_account(account_number) == masked_account_number