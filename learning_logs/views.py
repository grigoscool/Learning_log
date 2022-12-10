from django.shortcuts import render

def index(reguest):
    """Домашняя страница приложения learning_logs"""
    return render(reguest, 'learning_logs/index.html')  # функции представления