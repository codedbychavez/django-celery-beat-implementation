# django-celery-beat-implementation
A no bs approach to dynamic task scheduling in Django.


## Getting started

- Run `docker-compose up --build` in the main repo folder

- new prompt `cd djbeat`

- Start a Celery worker service

`celery -A djbeat worker --loglevel=info`

- new prompt `celery -A djbeat beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler`
