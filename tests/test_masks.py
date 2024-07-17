from src.masks import get_mask_card_number, get_mask_account
import pytest


@pytest.mark.parametrize(
    "card_number, masked_card_number",
    [
        ("1111222233334444", "1111 22** **** 4444"),
        ("", " Номер отсутствует"),
        ("jgcj", " Длина номера не верная или введены посторонние символы"),
        ("6576554433", " Длина номера не верная или введены посторонние символы"),
    ],
)
def test_get_mask_card_number(card_number, masked_card_number):
    assert get_mask_card_number(card_number) == masked_card_number


@pytest.mark.parametrize(
    "account_number, masked_account_number",
    [
        ("11112222333344445555", "** 5555"),
        ("", " Номер отсутствует"),
        ("jgcj", " Длина номера не верная или введены посторонние символы"),
        ("6576554433", " Длина номера не верная или введены посторонние символы"),
    ],
)
def test_get_mask_account(account_number, masked_account_number):
    assert get_mask_account(account_number) == masked_account_number
