# questionnaire
 Test company fabric


## Backend

_cd questionnaire_

_python -m venv env_

_cd venv/Scripts_

_activate.bat_

_pip install -r requirements.txt_

_python manage.py makemigrations_

_python manage.py migrate_

_python manage.py runserver_


## Документация по АПИ

/answer GET - Список опросов прошедших пользователем
/answer POST - Создание опроса с ответами пользователя

/interview GET - Список активных опросов
