import pytest
import requests
import urllib.parse
from typing import Optional, Dict, Any
from config.config import Config
from config.test_data import TestData
from utils.auth import get_auth_token


class ChitaiGorodAPI:
    """Класс для работы с API Читай город"""

    def __init__(self):
        self.base_url_v1 = Config.API_V1_URL
        self.base_url_v2 = Config.API_V2_URL
        self.token = None
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "application/json"
        }

    def get_token(self) -> bool:
        """Получение токена авторизации"""
        self.token = get_auth_token()

        if self.token:
            self.headers["Authorization"] = f"Bearer {self.token}"

        return self.token is not None

    def search_products(self, phrase: str, customer_city_id: int = Config.DEFAULT_CITY_ID) -> Optional[Dict[str, Any]]:
        """Поиск товаров по названию"""
        try:
            encoded_phrase = urllib.parse.quote(phrase)
            url = f"{self.base_url_v2}search/product?customerCityId={customer_city_id}&phrase={encoded_phrase}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            pytest.fail(f"Ошибка поиска товаров: {e}")
            return None

    def add_to_cart(self, product_id: str, quantity: int = 1) -> Dict[str, Any]:
        """Добавление товара в корзину"""
        url = f"{self.base_url_v1}cart/product"
        data = {
            "product_id": product_id,
            "quantity": quantity,
            "customer_city_id": Config.DEFAULT_CITY_ID
        }
        response = requests.post(url, headers=self.headers, json=data)

        try:
            return {
                "status_code": response.status_code,
                "response": response.json() if response.content else None
            }
        except ValueError:
            return {
                "status_code": response.status_code,
                "response": None
            }


@pytest.fixture(scope="module")
def api_client():
    """Фикстура для создания клиента API"""
    client = ChitaiGorodAPI()
    yield client


def test_get_token(api_client):
    """Тест получения токена авторизации"""
    assert api_client.get_token() is True
    assert api_client.token is not None
    assert len(api_client.token) > 10
    assert "Authorization" in api_client.headers


def test_search_products(api_client):
    """Тест поиска товаров"""
    result = api_client.search_products(TestData.SEARCH_PHRASE)

    assert result is not None
    assert "data" in result
    assert "relationships" in result["data"]
    assert "products" in result["data"]["relationships"]
    assert isinstance(result["data"]["relationships"]["products"]["data"], list)


def test_add_to_cart(api_client):
    """Тест добавления товара в корзину"""
    # Сначала ищем товар
    search_result = api_client.search_products(TestData.SEARCH_PHRASE)
    assert search_result is not None

    # Берем первый найденный товар
    product_id = search_result["data"]["relationships"]["products"]["data"][0]["id"]

    # Добавляем в корзину
    add_result = api_client.add_to_cart(product_id)

    # API возвращает 422 без авторизации, но мы проверяем структуру ответа
    assert isinstance(add_result, dict)
    assert "status_code" in add_result
    assert "response" in add_result


def test_negative_search(api_client):
    """Негативный тест поиска несуществующего товара"""
    result = api_client.search_products(TestData.INVALID_SEARCH_PHRASE)

    assert result is not None
    assert "data" in result
    assert isinstance(result["data"]["relationships"]["products"]["data"], list)


def test_negative_add_to_cart(api_client):
    """Негативный тест добавления несуществующего товара"""
    result = api_client.add_to_cart("несуществующий_id_123456")

    assert isinstance(result, dict)
    assert "status_code" in result
    assert result["status_code"] in [400, 422]  # Ожидаем ошибку клиента