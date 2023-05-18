from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    
    # определяем подкласс для создания выбираемых значений по аналогии с enum
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    # определяем поля класса они же будут соответствовать полям таблицы БД
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 2, choices=Status.choices, default=Status.DRAFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    
    
    class Meta:
        # автоматически задаем порядок сортировки выдачи данных из таблицы БД "от новых к старым"
        ordering = ['-publish']
        
        # определение индексирования поля в БД
        indexes = [
            models.Index(fields=['-publish']),
        ]
        

    def __str__(self) -> str:
        return self.title
    
    