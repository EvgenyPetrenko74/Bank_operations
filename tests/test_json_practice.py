import pytest


from src.json_practice import generate_users


@pytest.fixture
def city():
    return ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia"]


@pytest.fixture
def first_name():
    return ["John", "Jane", "Mark", "Emily", "Michael", "Sarah"]


@pytest.fixture
def last_name():
    return ["Doe", "Smith", "Johnson", "Brown", "Lee", "Wilson"]


def test_generate_users_first_names(first_name, last_name, city):
    """Проверяет, что имена сгенерированных пользователей находятся в исходном списке."""
    for i in range(5):
        assert next(generate_users(first_name, last_name, city))["first_name"] in first_name


def test_generate_users_last_names(first_name, last_name, city):
    """Проверяет, что фамилии сгенерированных пользователей находятся в исходном списке."""
    for i in range(5):
        assert next(generate_users(first_name, last_name, city))["last_name"] in last_name


def test_generate_users_cities(first_name, last_name, city):
    """Проверяет, что города сгенерированных пользователей находятся в исходном списке."""
    for i in range(5):
        assert next(generate_users(first_name, last_name, city))["city"] in city


def test_generate_users_age(first_name, last_name, city):
    """Проверяет, что возраст сгенерированных пользователей находятся в нужном диапазоне."""
    for i in range(5):
        assert next(generate_users(first_name, last_name, city))["age"] in range(18, 66)


# pytest tests/test_json_practice.py
