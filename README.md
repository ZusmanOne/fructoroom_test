# Сервис для хранения ссылок пользователя
Сервис, который хранит ссылки пользователей(закладки) на веб-сайты

## Описание
После регистрации в сервисе пользователь может создавать различные коллекции в которые будет добавлять свои закладки
(веб-страницы).

Одна и та же закладка может быть в одной или нескольких коллекциях сразу. 
Либо быть без коллекции

### Как запустить dev-версию
Скачайте код:
```sh
git clone https://github.com/ZusmanOne/fructoroom_test.git
```

Перейдите в каталог проекта:
```sh
cd fructoroom_test
```
[Установите Python](https://www.python.org/), если этого ещё не сделали.

Проверьте, что `python` установлен и корректно настроен. Запустите его в командной строке:
```sh
python --version
```

В каталоге проекта создайте виртуальное окружение:
```sh
python -m venv venv
```
Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`

Установите зависимости в виртуальное окружение:
```sh
pip install -r requirements.txt
```
Настройка: создать файл `.env` в каталоге `link_storage_service/` со следующими настройками:

- `DEBUG` — дебаг-режим. Поставьте `True`.
- `SECRET_KEY` — секретный ключ проекта. Он отвечает за шифрование на сайте. 
- `ALLOWED_HOSTS` —  localhost 127.0.0.1 [::1]
- `POSTGRES_NAME` - имя бд
- `POSTGRES_USER`- имя юзера
- `POSTGRES_PASSWORD`- пароль юзера
- `POSTGRES_PORT`-5432
- `DB_HOST` - localhost

Учтите, что для локального запуска сервиса, вам нужно предварительно создать локальную БД(postgres)


Примените миграции

```sh
python manage.py migrate
```

Создайте супер-пользователя
```sh
python manage.py createsuperuser
```

Запустить сервер
```sh
python manage.py runserver
```
По адресу ```http://127.0.0.1:8000/```  будет доступен сервис

Сервис имеют следующую маршрутизацию

```http://127.0.0.1:8000/``` - список эндпоинтов

```http://127.0.0.1:8000/registration/``` - регистрация юзера

```http://127.0.0.1:8000/create_page/``` - создание закладки 

```http://127.0.0.1:8000/pages/``` - список cуществующих страниц(закладок)

```http://127.0.0.1:8000/page/{pk}/``` - получение конкртеной закладки

```http://127.0.0.1:8000/collections/``` - получение всех коллекций

```http://127.0.0.1:8000/collection{pk}/``` - получение конкртеной коллекций


###  Описание разработанного API в Swagger

```http://127.0.0.1:8000/swagger``` 

```http://127.0.0.1:8000/docs/``` 



***
## Запуск тестов
``` 
 pytest storage/tests/test_api.py
```
### Сервис так же обернут в докер, что бы запустить проект в докере наберите команду:

``` 
docker-compose  up  --build
```
Данная команда предусматривает уже предустановленный docker, docker-compose


