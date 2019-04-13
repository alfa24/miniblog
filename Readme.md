miniblog - Площадка для блоггеров (Тестовое задание)

#### Стек технологий
* django 2
* gunicorn 
* postgress
* celery
* redis


#### Установка
* git clone https://github.com/alfa24/miniblog.git
* cd miniblog/src
* sudo docker-compose build
* sudo docker-compose up -d


#### Создать суперпользователя в базе
* sudo exec djangoapp python manage.py createsuperuser


#### Остановить сайт
* sudo docker-compose stop

Сайт будет доступен по адресу http://127.0.0.1:8000