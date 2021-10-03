# CNAB Parser

## Description

Flat file parser project to deal with large positional files, like CSV.

To accomplish the task of dealing with large batch processing files, the project has a RabbitMQ queue that asynchronously processes the file in a separate worker.

Sending the task to the queue is done by an RPC worker listening for processing requisitions. This worker lies inside an APScheduler command. It can be replaced by a CRON job instead.

## Modules

- Parser API
  - REST API for database operations
- Parser Django Command Worker
  - Django command for worker (to be loaded inside a systemd service)
- Parser Admin (Backend)
  - Django Admin application to help out CRUD operations
- Parser Database
  - PostgreSQL inside docker container (run docker-compose up to bring it up)
- Parser Web (Frontend)
  - React Web application for user interface

## Frontend Environment Setup

```
$ cd frontend
$ yarn
$ yarn start
```

Then navigate to `http://localhost:3000`

## Admin Backend

First you must bring the environment up.

Then navigate to `http://localhost:8000/admin`

Login as superuser.

## Environment Setup

- Git clone the project

```
$ git clone repo_address
```

- Change to new folder

```
$ cd folder_name
```

- Create and activate new virtual environment

```
$ virtualenv env
$ source env/bin/activate
```

- Install dependencies

```
$ pip install -r requirements.txt
```

- Start all services, including the database

Open a new terminal to type the following command:

```
$ docker-compose up
```

- Back to the first terminal, do the migration

```
$ python manage.py migrate
```

- Load the auxiliary tables

```
$ python manage.py loaddata campos_cnab import_cnab_template import_template tipos_transacoes
```

- Then create a superuser (you are going to need it later on)

```
$ python manage.py createsuperuser
```

- Now bring Dramatiq service up

```
$ source env/bin/activate
$ python manage.py rundramatiq
```

- Open a third command shell to bring APScheduler service up

```
$ source env/bin/activate
$ python manage.py runscheduler
```

- Open a last terminal to bring the Django web server up

```
$ source env/bin/activate
$ python manage.py runserver
```

## Database Reset

Sometimes is necessary clear up database and start over, to do so follow these commands:

```
$ docker-compose down
$ docker volume ls
$ docker volume rm desafio-dev_parser_volume
$ docker-compose up
```

> NOTE: Don't you forget to create a new superuser!

## Superuser Password Recovery

In case of superuser's password lost, first open a Django shell:

```
# source env/bin/activate
# python manage.py shell
```

Inside the shell, type following commands to set superuser with a new password:

```
>>> from django.contrib.auth.models import User
>>> user = User.objects.filter(is_superuser=True).first()
>>> user.set_password('newpas1234')
>>> user.save()
```

In case you also forgot the `username`, do the following:

```
>>> user.username
```

To exit, type:

```
>>> quit()
```
