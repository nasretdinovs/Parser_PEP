# Парсер документации Python
Парсинг статусов PEP с сайта https://peps.python.org/

## Установка

Клонируйте репозиторий.

Создайте и активируйте виртуальное окружение:

В Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

В Windows
```bash
python -m venv venv
source venv/Scripts/activate
```

Используйте [pip](https://pip.pypa.io/en/stable/)
для установки зависимостей.

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Запуск
Команда для запуска:
```
scrapy crawl pep
```
Результаты парсинга в папке **results**