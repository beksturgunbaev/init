from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('poslednie-novosti', views.news, name='news'),
    path('novosti/<str:pk>/', views.newsDetail, name='newsDetail'),
    path('nashi-dostizheniya', views.achievements, name='achievements'),
    path('sostav_kafedry/<str:pk>/', views.teachers, name='teachers'),
    path('raspisaniya', views.shedule, name='shedule'),
    path('o-kafedre', views.about, name='about'),
    path('magistratura', views.magistratura, name='Magistratura'),
    path('nomenklatura-del', views.nomenklatura, name='nomenklatura'),
]
