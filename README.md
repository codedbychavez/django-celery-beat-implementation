# Dynamic task scheduling
A no bs approach to dynamic task scheduling in Django.

## Overview
This application lets you configure dynamic periodic tasks in Django application.

This is made possible by the following major components:
- A RabbitMQ server running in docker
- A Celery worker
- A Beat scheduler service

## Features
- Periodic task scheduling via API Endpoints:
    - Create (/api/create)
    - Update (/api/update)
    - Delete (/api/delete)

## Requirements

It is required that all the items mentioned in the overview section be installed as well as the below. Luckily these are listed the requirements.txt file for you.

- Docker
- Python 3.8
- Virtualenv

See the following section:

## Getting started

1. Create a virtual environment using virtualenv (recommended) or using a similar tool of your choice.

2. `cd djbeat` folder and run `pip install -r requirements.txt`

3. Run `docker-compose up --build` in the main repo folder

4. In a new prompt run the following:

- `cd djbeat` (don't `cd` into the `djbeat` folder if you are already in this folder. TLDR; you need to be in the outermost one)

5. Start a Celery worker service. In a new prompt:
 
`celery -A djbeat worker --loglevel=info`

6. Start the beat service. In a new prompt
 
- `celery -A djbeat beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler`

### References

https://django-celery-beat.readthedocs.io/en/latest/
https://docs.celeryproject.org/en/latest/userguide/workers.html
https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#using-custom-scheduler-classes
https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#starting-the-scheduler

