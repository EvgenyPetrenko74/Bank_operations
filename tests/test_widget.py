from src.widget import mask_account_card, get_data
import pytest


@pytest.mark.parametrize(
    "input_string, output_string",
    [
        ("Visa platinum 1111222233334444", "Visa platinum 1111 22** **** 4444"),
        ("Maestro 1111222233334444", "Maestro 1111 22** **** 4444"),
        ("", "Данные отсутствуют или введены неверно"),
        ("jgcj", "Данные отсутствуют или введены неверно"),
        ("Счет 11112222333344445555", "Счет ** 5555"),
    ],
)
def test_mask_account_card(input_string, output_string):
    assert mask_account_card(input_string) == output_string


def test_get_data(data_string):
    assert get_data(data_string) == "11.07.2018"
