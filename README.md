# django-celery-beat-implementation
A no bs approach to dynamic task scheduling in Django.


## Getting started

- Run `docker-compose up --build` in the main repo folder

- In a new prompt run the following:

- `cd djbeat`

- Start a Celery worker service (**OPTIONAL**)
 
`celery -A djbeat worker --loglevel=info`

- Start the beat service. In a new prompt
 
- `celery -A djbeat beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler`
