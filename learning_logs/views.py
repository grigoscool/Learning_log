from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(reguest):
    """Домашняя страница приложения learning_logs"""
    return render(reguest, 'learning_logs/index.html')  # функции представления

def topics(request):
    """Выводит список тем"""
    topics = Topic.objects.order_by('date_added')   #запрос к БД на получение объектов Topic
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

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

def new_entry(request, topic_id):
    """Определяет новую запись"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            last_entry = form.save(commit=False)
            last_entry.topic = topic
            last_entry.save()
            return redirect('learning_logs:topic', topic_id = topic_id)
    context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        # Данные не отправлялись, создается пустая форма
        form = EntryForm(instance=entry)
    else:
        # Отправленные данные POST, обработать данные
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'topic':topic, 'entry': entry, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
