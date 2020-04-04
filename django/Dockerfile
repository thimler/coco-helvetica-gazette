FROM python:3.8

RUN apt-get update && apt-get install -y gettext

RUN pip install pipenv
COPY Pipfile* /app/
RUN cd /app && \
    pipenv lock --requirements > requirements.txt && \
    pip install -r requirements.txt

COPY . /app

WORKDIR /app

RUN django-admin compilemessages

# TODO: Switch this to a real server like Gunicorn + Nginx for static files
CMD python3 manage.py runserver 0.0.0.0:80

