from django.urls import path
from .views import *

urlpatterns = [
    # api paths
    path('create_interval_periodic_task', create_interval_periodic_task.as_view()),
    path('delete_interval_periodic_task', delete_interval_periodic_task.as_view()),
    path('update_interval_periodic_task', update_interval_periodic_task.as_view()),


]