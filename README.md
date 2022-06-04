# Проект YaMDb ![example workflow](https://github.com/AnastasiaNesterenko/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Учебный проект на подобии IMDb

### Описание

В данном проекте реализованы функции выставления оценок на произведения,
написание рецензий, написание комментариев к рецензиям.

### Шаблон наполнения env-файла

DB_ENGINE= указываем, что работаем с какой базой данных работаем<br/>
DB_NAME= имя базы данных<br/>
POSTGRES_USER= логин для подключения к базе данных<br/>
POSTGRES_PASSWORD= пароль для подключения к БД<br/>
DB_HOST= название сервиса (контейнера)<br/>
DB_PORT= порт для подключения к БД <br/>

### Как запустить проект
Запустить контейнер из папки infra/

```
sudo docker-compose up -d --build
```

Выполнить миграции:
```
sudo docker-compose exec web python manage.py migrate
```

Создать суперпользователя
```
sudo docker-compose exec web python manage.py createsuperuser
```

Сборка статистики:
```
sudo docker-compose exec web python manage.py collectstatic --no-input 
```

Запустить скрипт для заполнения БД данными.
Файл расположен \api_yamdb\static\data\csvinbd.py
```
ПКМ -> Run csvinbd
```

Запустить проект:
```
python manage.py runserver
```
Или вручную заполнить:)

### Автор

Нестеренко Анастасия

[ссылка на гит](https://github.com/AnastasiaNesterenko "Переходи обязательно")


