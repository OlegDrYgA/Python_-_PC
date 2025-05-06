# Автотесты для сайта "Читай город"

Этот проект содержит автоматизированные тесты для веб-сайта "Читай город", включая UI и API тесты.
Работа выполнена на основе курсовой работы по ручному тестированию :
https://olegdryga.yonote.ru/doc/otchet-o-testirovanii-sajta-i-web-prilozheniya-chitaj-gorod-vypolnil-student-gr-qa-892-dryga-or-dSiBS2iBE7


## Структура проекта
project/
├── config/ # Конфигурационные файлы
│ ├── init.py
│ ├── config.py # Настройки окружения (URL, таймауты)
│ └── test_data.py # Тестовые данные
├── tests/ # Тесты
│ ├── init.py
│ ├── test_api.py # API-тесты
│ └── test_ui.py # UI-тесты
├── utils/ # Вспомогательные утилиты
│ ├── init.py
│ └── auth.py # Функции для работы с авторизацией
├── requirements.txt # Зависимости Python
└── README.md # Документация

## Установка и настройка

1. Клонируйте репозиторий:
   ```bash
   git clone <repository-url>
   cd <D:\CSKY-PRO-учеба\PYTHON_&_PC\Diplom_avtotest_Chitai_gorod>
   
установите зависимости pip install -r requirements.txt

Запуск всех тестов pytest Diplom_avtotest_Chitai_gorod/tests
Запуск API тестов pytest Diplom_avtotest_Chitai_gorod/tests/test_api.py   
Запуск Ui тестов pytest pytest Diplom_avtotest_Chitai_gorod/tests/test_ui.py
Запуск отчетов ALLURE  pytest --alluredir=allure-results
Просмотр результатов allure serve allure-results
