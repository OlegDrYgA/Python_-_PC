import requests
import pytest
from config.config import Config


def get_auth_token() -> str:
    """Получение токена авторизации"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/json"
    }

    try:
        response = requests.get(Config.BASE_URL, headers=headers)
        raw_token = response.cookies.get('access-token')
        token = raw_token[9:] if raw_token and len(raw_token) > 9 else None

        if not raw_token:
            pytest.fail("Токен не найден в куках")

        if not token:
            pytest.fail("Не удалось получить токен авторизации")

        return token
    except Exception as e:
        pytest.fail(f"Ошибка получения токена: {e}")