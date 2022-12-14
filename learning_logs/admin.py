from django.contrib import admin

from .models import Topic, Entry

class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'date_added']
    list_display_links = ['text']
    search_fields = ['text']
class EntryAdmin(admin.ModelAdmin):
    list_display = ['text', 'date_added']
    list_display_links = ['text']
    search_fields = ['text']

admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, EntryAdmin)