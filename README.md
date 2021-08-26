
___
## Для запуска проекта необходимо:
___

* #### Необходимо создать clone репозитория

`git clone https://github.com/KirillGu/django_dip`

* #### Установить зависимости:

`pip install -r requirements.txt`

* #### Импортировать фикстуры

`python manage.py loaddata fixtures/fixtures.json`

* #### Необходимо будет создать базу в postgres и прогнать миграции

`python manage.py migrate`

* #### Запустить проект

`python manage.py runserver`

* #### Интерфейс администратора

`127.0.0.1/8000/admin/`

Login: admin | Password: admin
