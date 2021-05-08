from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('novosti', views.news, name='news'),
    path('sostav_kafedry', views.teachers, name='teachers'),
]
