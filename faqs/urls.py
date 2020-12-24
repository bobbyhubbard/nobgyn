from django.urls import path
from faqs import views

app_name = 'faqs'
urlpatterns = [
    path('', views.index, name='index'),
    path('obstetrics', views.ob, name='Obstetrics'),
    path('gynecology', views.gyn, name='Gynecology'),
    path('postoperative', views.postop, name='Postoperative'),
    path('<slug:slug>', views.faqDetail, name='detail'),
]
