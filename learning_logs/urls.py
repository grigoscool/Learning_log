'''Определяет схемы URL lkz learning_logs'''
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # домашняя страница
    path('', views.index, name = 'index'),
]
