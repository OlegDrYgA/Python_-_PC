import pytest
from String_Utils import StringUtils


utils = StringUtils()

def test_capitalize(): # позитивные тесты на строчную букву
        assert utils.capitalize("skypro") == "Skypro"
        assert utils.capitalize("hi everyone") == "Hi everyone"
        assert utils.capitalize("") == ""
@pytest.mark.skip
def test_trim():  # убирает лишние пробелы позитивные тесты
        assert utils.trim("   skypro") == "skypro"
        assert utils.trim("hello   ") == "hello" #Негативный тест
        assert utils.trim("   ") == ""
        assert utils.trim("noLeadingSpaces") == "noLeadingSpaces"

def test_to_list(): # создает список строк из набора с различными разделителями
        assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
        assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]
        assert utils.to_list("") == []
        assert utils.to_list("a,b,c,d,", ",") == ["a", "b", "c", "d", ""]

def test_contains(): #Поиск нужного символа
        assert utils.contains("SkyPro", "S")
        assert not utils.contains("SkyPro", "U")  #негативные тест
        assert not utils.contains("", "A")   #негативные тест

def test_delete_symbol(): # Исключение заданного символа
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
        assert utils.delete_symbol("Hello World!", "!") == "Hello World"
        assert utils.delete_symbol("", "x") == ""

def test_starts_with():  #Определение отвечает ли первый символ заданному
        assert utils.starts_with("SkyPro", "S")
        assert not utils.starts_with("SkyPro", "P")
        assert not utils.starts_with("", "A")

#Негативные   тесты
def test_end_with():
        assert utils.end_with("SkyPro", "o")
        assert not utils.end_with("SkyPro", "y")
        assert not utils.end_with("", "A")

def test_is_empty():
        assert utils.is_empty("")
        assert utils.is_empty(" ")
        assert not utils.is_empty("SkyPro")


def test_list_to_string(): # Объединение в строку
        assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
        assert utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
        assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
        assert utils.list_to_string([]) == ""
#Негативные тесты

def test_capitalize_empty_string():
    result = utils.capitalize("")
    assert result == "", "Ожидается, что пустая строка останется пустой"
@pytest.mark.skip
def test_trim_none():
    result = utils.trim(None)
    assert result is None, "Ожидается, что None останется None"
@pytest.mark.skip
def test_contains_non_string_input():
    result = utils.contains(12345, "1")
    assert result is False