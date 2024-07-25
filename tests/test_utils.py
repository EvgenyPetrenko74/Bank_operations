import json
from unittest.mock import mock_open, patch
from src.utils import get_info


@patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
def test_get_info_success(mock_file):
    expected_result = {"key": "value"}
    result = get_info("dummy_file.json")
    assert result == expected_result

@patch("builtins.open", side_effect=FileNotFoundError("No such file or directory: 'dummy_file.json'"))
def test_get_info_file_not_found(mock_file):
    expected_result = []
    result = get_info("dummy_file.json")
    assert result == expected_result

@patch("builtins.open", new_callable=mock_open, read_data='invalid json')
def test_get_info_invalid_json(mock_file):
    expected_result = []
    result = get_info("dummy_file.json")
    assert result == expected_result

# Запуск тестов
if __name__ == "__main__":
    test_get_info_success()
    test_get_info_file_not_found()
    test_get_info_invalid_json()
    print("All tests passed.")
