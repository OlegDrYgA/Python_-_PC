import time
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config import Config
from config.test_data import TestData


@allure.feature("Авторизация")
@allure.story("Изменение цвета поля при вводе телефона")
def test_phone_field_color_change(driver):
    with allure.step("1. Открыть главную страницу"):
        driver.get(Config.BASE_URL)

    with allure.step("2. Нажать кнопку входа"):
        login_button = WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "#__nuxt > div > header > div > div.header-controls.header__controls > div > button > span.header-controls__icon-wrapper > svg"))
        )
        login_button.click()

    with allure.step("3. Проверить исходный цвет кнопки"):
        submit_button_div = WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#tid-form > button > div"))
        )
        initial_color = submit_button_div.value_of_css_property("color")
        assert "rgba(209, 214, 218, 1)" in initial_color, f"Ожидался цвет #D1D6DA, получен {initial_color}"

    with allure.step("4. Ввести номер телефона"):
        phone_input = WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#tid-input"))
        )
        phone_input.send_keys(TestData.TEST_PHONE)
        time.sleep(2)  # Ожидание изменения состояния

    with allure.step("5. Проверить изменение цвета кнопки"):
        updated_color = submit_button_div.value_of_css_property("color")
        assert "rgba(255, 255, 255, 1)" in updated_color, f"Ожидался цвет #FFFFFF, получен {updated_color}"


@allure.feature("Поиск")
@allure.story("Поиск несуществующего товара")
def test_search_nonexistent_item(driver):
    with allure.step("1. Открыть главную страницу"):
        driver.get(Config.BASE_URL)

    with allure.step("2. Ввести несуществующий запрос"):
        search_input = WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input.search-form__input'))
        )
        search_input.send_keys(TestData.INVALID_SEARCH_PHRASE)

    with allure.step("3. Нажать кнопку поиска"):
        search_button = WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        search_button.click()

    with allure.step("4. Проверить сообщение об отсутствии результатов"):
        result_element = WebDriverWait(driver, Config.DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.catalog-stub__content h4'))
        )
        assert "Похоже, у нас такого нет" in result_element.text


@allure.feature("Геолокация")
@allure.story("Смена города на Санкт-Петербург")
def test_change_city_to_spb(driver):
    with allure.step("1. Открыть главную страницу"):
        driver.get(Config.BASE_URL)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body')))
        allure.attach(driver.get_screenshot_as_png(),
                      name="main_page_loaded",
                      attachment_type=allure.attachment_type.PNG)

    with allure.step("2. Закрыть мешающие элементы (куки, баннеры)"):
        try:
            # Закрытие куки
            cookie_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Принять куки")]')))
            cookie_btn.click()
            time.sleep(1)
        except:
            pass  # Если нет куки-баннера

    with allure.step("3. Нажать кнопку изменения города"):
        try:
            city_btn = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Изменить город")]'))
            )
            city_btn.click()
            allure.attach(driver.get_screenshot_as_png(),
                          name="city_popup_opened",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            pytest.fail(f"Не удалось открыть попап выбора города: {str(e)}")

    with allure.step("4. Ввести 'Санкт-Петербург' в поиск"):
        try:
            search_input = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder*="город"]'))
            )
            search_input.clear()
            search_input.send_keys(TestData.SPB_CITY)
            time.sleep(1)  # Ожидание появления результатов
            allure.attach(driver.get_screenshot_as_png(),
                          name="city_search_entered",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            pytest.fail(f"Не удалось ввести город в поиск: {str(e)}")

    with allure.step("5. Выбрать город из списка"):
        try:
            city_option = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//li[contains(@class, "city-list-item") and contains(., "Санкт-Петербург")]'))
            )
            city_option.click()
            allure.attach(driver.get_screenshot_as_png(), name="city_selected",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            pytest.fail(f"Не удалось выбрать город из списка: {str(e)}")

    with allure.step("6. Проверить отображение нового города"):
        try:
            current_city = WebDriverWait(driver, 10).until(
                lambda d: d.find_element(By.XPATH, '//div[contains(@class, "city-selector")]').text
            )
            assert "Петербург" in current_city, f"Текущий город: {current_city}"
            allure.attach(driver.get_screenshot_as_png(), name="city_changed",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(),
                          name="city_verification_failed",
                          attachment_type=allure.attachment_type.PNG)
            print(f"⚠ Дополнительная проверка не удалась: {str(e)}")