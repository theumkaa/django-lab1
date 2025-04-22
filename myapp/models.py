from django.db import models
class Task(models.Model):
    title = models.CharField(max_length=255) # Название задачи
    description = models.TextField(blank=True, null=True) # Описание
    created_at = models.DateTimeField(auto_now_add=True) # Дата создания
    rashod= models.DecimalField(max_digits=10, decimal_places=2) # Расход
    status = models.CharField(max_length=50, choices=[('new', 'New'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='new') # Статус задачи
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE) # Связь с пользователем
    def __str__(self):
        return self.title