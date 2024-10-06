import uuid
from django.db import models
from django.contrib.auth.models import User # Модель пользователя, которую предоставляет сам Django

# Все модели которые должны отображаться в БД - наследуют класс Model
class Task(models.Model):
    # Поля
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model

    # здесь определяется мета информация такая как:
    # Индексы, ограничения, название таблицы

    # (подробнее тут: https://docs.djangoproject.com/en/5.1/ref/models/options/)
    class Meta:
        db_table_comment = "Question answers"

    def __str__(self):
        return self.title