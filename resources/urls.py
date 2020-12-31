from django.urls import path
from . import views

app_name = 'resources'
urlpatterns = [
    path('', views.index, name='index'),
    path('forms_information', views.forms_information, name='forms_information'),
    path('health_plans', views.health_plans, name='health_plans'),
]
