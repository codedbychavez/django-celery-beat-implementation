from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django_celery_beat.models import PeriodicTask, IntervalSchedule, PeriodicTasks

# Create your views here.


class create_interval_periodic_task(APIView):
    """
    Create an interval-based periodic task
    Expected request object looks like the below
    {
        "interval": 10,
        "period_choice": "seconds",
        "name": "create print_hello",
        "task": "djbeat.api.celery_init.print_hello"
    }
    """
    def post(self, request, *args, **kwargs):
        interval = request.data['interval']
        period_choice = get_period_choice(request.data['period_choice'])
        name = request.data['name']
        task = request.data['task']

        # Switch for period choices
        if period_choice == 'DAYS':
            schedule, created = IntervalSchedule.objects.get_or_create(every=interval, period=IntervalSchedule.DAYS)
            # CREATE PERIODIC TASK
            PeriodicTask.objects.create(name=name, task=task, interval=schedule)

        elif period_choice == 'HOURS':
            schedule, created = IntervalSchedule.objects.get_or_create(every=interval, period=IntervalSchedule.HOURS)
            # CREATE PERIODIC TASK
            PeriodicTask.objects.create(name=name, task=task, interval=schedule)

        elif period_choice == 'MINUTES':
            schedule, created = IntervalSchedule.objects.get_or_create(every=interval, period=IntervalSchedule.MINUTES)
            # CREATE PERIODIC TASK
            PeriodicTask.objects.create(name=name, task=task, interval=schedule)

        elif period_choice == 'SECONDS':
            schedule, created = IntervalSchedule.objects.get_or_create(every=interval, period=IntervalSchedule.SECONDS)
            # CREATE PERIODIC TASK
            PeriodicTask.objects.create(name=name, task=task, interval=schedule)
     
     

        elif period_choice == 'MICROSECONDS':
            schedule, created = IntervalSchedule.objects.get_or_create(every=interval, period=IntervalSchedule.MICROSECONDS)
            # CREATE PERIODIC TASK
            PeriodicTask.objects.create(interval=schedule, name=name, task=task)


        user_message = 'Created an interval-based periodic task'
        print(user_message)
        return Response(user_message, status=status.HTTP_200_OK)

class delete_interval_periodic_task(APIView):
    """
    Delete an interval-based periodic task
    Expected request object looks like the below (Id of interval period task)
    {
        "id": 10, 
    }
    """
    def post(self, request, *args, **kwargs):
        periodic_task_id = request.data['id']
        periodic_task = PeriodicTask.objects.get(id=periodic_task_id)
        periodic_task.delete()
        user_message = 'Deleted an interval-based periodic task'
        print(user_message)
        return Response(user_message, status=status.HTTP_200_OK)


class update_interval_periodic_task(APIView):
    """
    Create an interval-based periodic task
    Expected request object looks like the below
    {
        "interval": 10,
        "period_choice": "seconds",
        "name": "update print hello",
        "task": "djbeat.api.celery_init.print_hello_update"
    }
    """
    def post(self, request, *args, **kwargs):
        print(request.data)
        periodic_task_id = request.data['id']
        interval = request.data['interval']
        period_choice = get_period_choice(request.data['period_choice'])
        name = request.data['name']
        task = request.data['task']


        # SWITCH FOR PERIOD CHOICES

        if period_choice == 'DAYS':
            # Get the schedule instance
            schedule_instance = PeriodicTask.objects.get(id=periodic_task_id)
            
            schedule_instance_id = schedule_instance.interval.id

            # Update the schedule
            IntervalSchedule.objects.filter(id=schedule_instance_id).update(every=interval, period=IntervalSchedule.DAYS)

            # Update the periodic task
            PeriodicTask.objects.filter(id=periodic_task_id).update(name=name, task=task)

        elif period_choice == 'HOURS':
            # Get the schedule instance
            schedule_instance = PeriodicTask.objects.get(id=periodic_task_id)
            
            schedule_instance_id = schedule_instance.interval.id

            # Update the schedule
            IntervalSchedule.objects.filter(id=schedule_instance_id).update(every=interval, period=IntervalSchedule.HOURS)

            # Update the periodic task
            PeriodicTask.objects.filter(id=periodic_task_id).update(name=name, task=task)

        elif period_choice == 'MINUTES':
            # Get the schedule instance
            schedule_instance = PeriodicTask.objects.get(id=periodic_task_id)
            
            schedule_instance_id = schedule_instance.interval.id

            # Update the schedule
            IntervalSchedule.objects.filter(id=schedule_instance_id).update(every=interval, period=IntervalSchedule.MINUTES)

            # Update the periodic task
            PeriodicTask.objects.filter(id=periodic_task_id).update(name=name, task=task)

        elif period_choice == 'SECONDS':
            # Get the schedule instance
            schedule_instance = PeriodicTask.objects.get(id=periodic_task_id)
            
            schedule_instance_id = schedule_instance.interval.id

            # Update the schedule
            IntervalSchedule.objects.filter(id=schedule_instance_id).update(every=interval, period=IntervalSchedule.SECONDS)

            # Update the periodic task
            PeriodicTask.objects.filter(id=periodic_task_id).update(name=name, task=task)

        elif period_choice == 'MICROSECONDS':
            # Get the schedule instance
            schedule_instance = PeriodicTask.objects.get(id=periodic_task_id)
            
            schedule_instance_id = schedule_instance.interval.id

            # Update the schedule
            IntervalSchedule.objects.filter(id=schedule_instance_id).update(every=interval, period=IntervalSchedule.MICROSECONDS)

            # Update the periodic task
            PeriodicTask.objects.filter(id=periodic_task_id).update(name=name, task=task)


        user_message = 'Updated an interval-based periodic task'
        print(user_message)
        return Response(user_message, status=status.HTTP_200_OK)

# Helper functions
def get_period_choice(period_choice):
    return period_choice.upper()