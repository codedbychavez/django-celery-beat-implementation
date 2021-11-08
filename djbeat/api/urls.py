from django.urls import path
from .views import *

urlpatterns = [
    # api paths
    path('create', create.as_view()),
]