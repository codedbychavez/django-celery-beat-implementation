from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django_celery_beat.models import PeriodicTask, IntervalSchedule, PeriodicTasks

# Create your views here.


class create(APIView):
    """
    Create an interval-based periodic task
    {
        "interval": 5, # Numeric interval period -> used to create an interval
        "period_choice: DAYS, HOURS, MINUTES, SECONDS, MICROSECONDS
        ""
    }
    """
    def post(self, request, *args, **kwargs):
        interval = request.data['interval']
        period_choice = get_period_choice(request.data['period_choice'])

        if period_choice == 'DAYS':
            schedule, created = IntervalSchedule.objects.get_or_create(every=interval, period=IntervalSchedule.SECONDS)

        if period_choice == 'HOURS':
            schedule, created = IntervalSchedule.objects.get_or_create(every=interval, period=IntervalSchedule.HOURS)

        print(IntervalSchedule.PERIOD_CHOICES)
        
        

        # CREATE PERIODIC TASK
        # PeriodicTasks.objects.create()
        user_message = 'Created an interval-based periodic task'
        print(user_message)
        return Response(user_message, status=status.HTTP_200_OK)

def get_period_choice(period_choice):
    return period_choice.upper()