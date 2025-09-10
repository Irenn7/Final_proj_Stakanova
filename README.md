# Final_proj_Stakanova
Тестирование UI/API
## Шаблон для автоматизации тестирования на Python

### Шаги:
1. Склонировать проект 'git clone https://github.com/Irenn7/Final_proj_Stakanova.git'
2. Установить все зависимости
3. Запустить все тесты с генерацией allure-данных
pytest --alluredir=allure-results
4. Запустить АПИ тесты pytest test/test_api_module.py --alluredir=allure-results
5. Запустить UI тесты pytest test/test_ui_module.py --alluredir=allure-results
6. Сгенерировать отчет 'allure generate allure-files -o allure-report' 
7. Открыть отчет 'allure open allure-report'

### Стек:
- pytest
- selenium
- requests
- allure
- config
- _sqlalchemy_

### Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API

### Полезные ссылки:
- [Подсказка по Markdown](https://www.markdownguide.org/cheat-sheet/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)

### Библиотеки:
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install requests
- pip install allure-pytest
- pip install -r requirements.txt
