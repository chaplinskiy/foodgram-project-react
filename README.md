# chaplinskiy/foodgram_project_react
![foodgram](https://github.com/chaplinskiy/foodgram-project-react/workflows/foodgram.yml/badge.svg)
## Дипломный проект факультета бэкенд-разработки [Яндекс.Практикума](https://practicum.yandex.ru/backend-developer)

### Описание:
С помощью сервиса Foodgram можно публиковать рецепты, подписываться на других пользователей, фильтровать рецепты по тегам, добавлять понравившиеся рецепты в избранное и скачивать файл со списком продуктов.

### Стек
```
Python 3
Django
Django REST Framework
Djoser
Docker
Nginx
Postgres
```
## Подготовка к развертыванию:
- Клонировать проект по адресу: https://github.com/chaplinskiy/foodgram-project-react.git
- Разжиться VPS-сервером (например, на [Яндекс.Облаке](cloud.yandex.ru/))
- Раскатать по серверу Убунту
- Убедиться, что на вашем сервере настроен ssh-доступ по публичному ключу и passphrase
- Установить на сервер Docker (предполагается, что y вас на сервере Ubuntu):
    ```bash
    sudo apt install docker.io
    ```
- и docker-compose (см. [руководство по установке](https://docs.docker.com/compose/install/)):
    ```bash
    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    ```
    ```bash
    sudo chmod +x /usr/local/bin/docker-compose
    ```
- отредактировать файл ```.github/workflows/foodgram.yml``` в соответствии со своими настройками, создать соответствующие Гитхаб-секретики
- Сделать 
    ```bash
    git commit && git push
    ``` 
    и наслаждаться результатом.

### Документация API с примерами:

```json
/api/docs/
```

### шаблон наполнения env-файла
см.
```bash
.env.template
```

### реквизиты для входа под суперпользователем
```
email: im@review.er
password: Q1w2e3r4t5y
```

### Демо рабочего проекта:
[51.250.64.153](http://51.250.64.153/)

(*адрес работает до первой перезагрузки, естественно*)

### Другие проекты автора:
https://github.com/chaplinskiy/
