from django.urls import path
from faqs import views

app_name = 'faqs'
urlpatterns = [
    path('', views.index, name='index'),
    path('faq_ob/<slug:old_path>.php', views.redirectFAQ),
    path('faq_gyn/<slug:old_path>.php', views.redirectFAQ),
    path('faq_postop/<slug:old_path>.php', views.redirectFAQ),
    path('obstetrics', views.ob, name='Obstetrics'),
    path('gynecology', views.gyn, name='Gynecology'),
    path('postoperative', views.postop, name='Postoperative'),
    path('<slug:slug>', views.faqDetail, name='detail'),
]
