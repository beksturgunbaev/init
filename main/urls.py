from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('poslednie-novosti', views.news, name='news'),
    path('novosti/<str:pk>/', views.newsDetail, name='newsDetail'),
    path('sostav_kafedry/<str:pk>/', views.teachers, name='teachers'),
]
