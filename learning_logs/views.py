from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

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
    content = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', content)

def new_topic(request):
    """Определяет новую тему"""
    if request.method != 'POST':
        # Данные не отправлялись, создается пустая форма
        form = TopicForm()
    else:
        # Отправленные данные POST, обработать данные
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)