# Web Form

1. [Подготовка к запуску](#start)

    1.1. [Настройка переменных окружения](#env)

    1.2. [Запуск сервера локально](#local)

2. [Cтэк технологий](#stack)
3. [Примеры запросов](#request)

# 1. Подготовка к запуску <a id="start"></a>

Примечание: использование Docker, poetry.


## 1.1. Настройка переменных окружения <a id="env"></a>

Перед запуском проекта необходимо создать копию файла
```.env.example```, назвав его ```.env``` и установить значение базы данных почты и тд.

### Системные требования
- Python 3.11+;
- Docker (19.03.0+) c docker compose;
- [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer);

Установка зависимостей poetry:

```shell
poetry install
```

## 1.2. Запуск сервера локально <a id="local"></a>

Запуск сервера локально:

1. запустите сервер:
```shell
make server-init
```

2. запустите работу контейнеров:
```shell
make start
```


# 2 Cтэк технологий <a id="stack"></a>

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/3.0.x/)
[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Poetry](https://img.shields.io/badge/Poetry-464646?style=flat-square&logo=Poetry)](https://python-poetry.org/)


# 3 Примеры запросов <a id="request"></a>

## Удачные пост запросы:
```shell
http://127.0.0.1:5000/get_form?email=1fe@gmail.com&date=21.11.2002

{
    "template_name": "Form-5"
}

http://127.0.0.1:5000/get_form?email=1fe@gmail.com&date=21.11.2002&text=text&phone=71111111111

{
  "template_name": "Form-15"
}
```
## пост запросы с ошибочными типами:

```shell
http://127.0.0.1:5000/get_form?date=1fe@gmail.com&email=21.11.2002&phone=text&text=71111111111

{
  "date": "email_type",
  "email": "date_type",
  "phone": "text_type",
  "text": "phone_type"
}

http://127.0.0.1:5000/get_form?test1=11.11.1111&test2=%2B71111111111&test3=text&test4=test@test.com

{
  "test1": "date_type",
  "test2": "phone_type",
  "test3": "text_type",
  "test4": "email_type"
}
```