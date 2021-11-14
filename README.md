# Dynamic task scheduling
A no bs approach to dynamic task scheduling in Django.

## Overview
This application lets you configure dynamic periodic tasks in Django application.

## Features
- Periodic task scheduling via API Endpoints:
    - Create (/api/create)
    - Update (/api/update)
    - Delete (/api/delete)

## Requirements
- Docker
- Python 3.8

## Getting started

- Run `docker-compose up --build` in the main repo folder

- In a new prompt run the following:

- `cd djbeat`

- Start a Celery worker service
 
`celery -A djbeat worker --loglevel=info`

- Start the beat service. In a new prompt
 
- `celery -A djbeat beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler`

### References

https://django-celery-beat.readthedocs.io/en/latest/
https://docs.celeryproject.org/en/latest/userguide/workers.html
https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#using-custom-scheduler-classes
https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#starting-the-scheduler

