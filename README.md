# questionnaire
 Test company fabric


## Docker

_cd questionnaire_

_docker-compose up --build_

_http://127.0.0.1:8000/_

## Server

_cd questionnaire_

_python -m venv env_

_cd venv/Scripts_

_activate.bat_

_pip install -r requirements.txt_

_python manage.py makemigrations_

_python manage.py migrate_

_python manage.py runserver_

_http://127.0.0.1:8000/_


## Документация по АПИ

/interview-user GET - Список опросов с ответами прошедших пользователем
/interview-user POST - Создание опроса пользователя

/interview GET - Список активных опросов
