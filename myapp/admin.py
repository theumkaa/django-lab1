from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # поля в списке
    search_fields = ('title',)              # строка поиска
    list_filter = ('created_at',)           # фильтр справа
