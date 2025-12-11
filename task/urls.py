from django.urls import path
from .views import task_list, task_create

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
]
