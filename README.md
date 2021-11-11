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

### References

https://django-celery-beat.readthedocs.io/en/latest/
https://docs.celeryproject.org/en/latest/userguide/workers.html
https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#using-custom-scheduler-classes
https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#starting-the-scheduler

