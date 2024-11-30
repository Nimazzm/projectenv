from django.urls import path
from .views import task, project, home

urlpatterns = [
    path('', home, name='home'),
    path('task/', task, name='task'),
    path('project/', project, name='project'),
]