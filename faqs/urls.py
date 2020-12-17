from django.urls import path
from . import views

app_name = 'faqs'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.faqDetail, name='detail')
]
