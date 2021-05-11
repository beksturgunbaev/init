from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('novosti', views.news, name='news'),
    path('sostav_kafedry/<str:pk>/', views.teachers, name='teachers'),
]
