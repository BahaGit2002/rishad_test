# Test app for Rishad

## Настройка

Первое, что нужно сделать, это клонировать репозиторий:

```sh
$ git clone https://github.com/BahaGit2002/rishad_test.git

$ cd rishad_test
```
После этого создать файл .env. Пример файла .env_example

Создат static папку

```sh
mkdir static
```
## Запуск
На Docker с docker-compose:

```sh
$ docker-compose up -d
```
И перейдите к `http://localhost`.

## Admin:

```sh
$ docker-compose exec web python manage.py createsuperuser
```
Чтоб зайти в админку: перейдите к `http://localhost/admin`.

## Алгоритм первых действий в Stripe 

Начале нужно создать Item, и потом перейдите к `http://localhost/item/{id}`
и нажмите кнопку buy.

Потом нужно создать Order `http://localhost/order_detail/{id}`
и нажмите кнопку buy.



