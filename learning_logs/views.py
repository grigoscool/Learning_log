from django.shortcuts import render

from .models import Topic


def index(reguest):
    """Домашняя страница приложения learning_logs"""
    return render(reguest, 'learning_logs/index.html')  # функции представления

def topics(request):
    """Выводит список тем"""
    topics = Topic.objects.order_by('date_added')   #запрос к БД на получение объектов Topic
    content = {'topics': topics}
    return render(request, 'learning_logs/topics.html', content)

def topic(request, topic_id):
    """Выводит одну тему и все ее записи"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    content = {'topics': topics, 'entries': entries}
    return render(request, 'learning_logs/topic.html', content)