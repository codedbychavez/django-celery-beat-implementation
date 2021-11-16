

from django.urls import path
from .views import *

urlpatterns = [
    # api paths
    path('create', create_interval_periodic_task.as_view()),
    path('update', update_interval_periodic_task.as_view()),
    path('delete', delete_interval_periodic_task.as_view()),

]