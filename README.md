# Final_proj_Stakanova
Тестирование UI/API
## Шаблон для автоматизации тестирования на Python

### Шаги:
1. Склонировать проект 'git clone https://github.com/Irenn7/Final_proj_Stakanova.git'
2. Установить все зависимости
3. Запустить тесты 'pytest'
4. Запустить АПИ тесты cd test pytest test_api_module.py
5. Запустить UI тесты cd test pytest test_ui_module.py 
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
- ./bd - хелперы для работы с BD

### Полезные ссылки:
- [Подсказка по Markdown](https://www.markdownguide.org/cheat-sheet/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)

### Библиотеки:
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install requests
- pip install allure-pytest
- 
