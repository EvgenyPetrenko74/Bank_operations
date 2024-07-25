import json
from unittest.mock import patch
from src.external_api import all_amount_rub_convert, transaction, empty_dict


@patch("src.external_api.requests.request")
def test_all_amount_rub_convert_successfull(mocked_request):
    mocked_request.return_value.json.return_value = {"result": "100"}
    assert all_amount_rub_convert(transaction) == "100"


@patch("src.external_api.requests.request")
def test_all_amount_rub_convert_error(mocked_request):
    mocked_request.return_value.json.return_value = {"result": "100"}
    assert all_amount_rub_convert(empty_dict) == 0.0


# pytest tests/test_external_api.py
