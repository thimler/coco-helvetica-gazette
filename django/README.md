# Coco Helvetica Gazette

Django 3 project running on python 3.8 with Pipenv

## Requirement

- Python 3
- pip3
- pipenv

See [this documentation](https://pipenv-fork.readthedocs.io/en/latest/install.html) to install pipenv

## Setup your project
Clone the repository

    git@github.com:antoinealb/coco-helvetica-gazette.git

Go into the `django` folder

    cd coco-helvetica-gazette/django

Install python dependencies

    pipenv install

Go into your virtual environment

    pipenv shell

Run the migrations

    python manage.py migrate

Run the python dev server

    python manage.py runserver

Then open this link in your browser to see the project in action [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Running with Docker

```
docker build -t coco .
docker run -it -p 8000:80 coco
```

Then open this link in your browser to see the project in action [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Unfortunately, this breaks django live reload, so you have to kill and start the server process for your changes outside the container to take effect.
