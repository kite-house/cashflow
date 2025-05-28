# Веб-сервис для управления движением денежных средств (ДДС)

### Установка зависимостей

> pip install -r requirements.txt

### Настройка базы данных

> python manage.py createsuperuser

> Переходим в /admin и заполняем нужные данные( статусы, типы и тд...)

### Запускаем 

> python manage.py runserver

### Доступные точки

```
    "admin panel" : "http://127.0.0.1:8000/admin/"
    "api/record": "http://127.0.0.1:8000/api/record/",
    "api/status": "http://127.0.0.1:8000/api/status/",
    "api/type": "http://127.0.0.1:8000/api/type/",
    "api/category": "http://127.0.0.1:8000/api/category/",
    "api/subcategory": "http://127.0.0.1:8000/api/subcategory/"

```