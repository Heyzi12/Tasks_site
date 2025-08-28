from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [
        ("Low" , "Низький пріорітет"),
        ("Medium" , "Середній пріорітет"),
        ("High" , "Високий пріорітет"),
    ]
    STATUS_CHOICES = [
        ("Pending" , "Потрібно виконати"),
        ("In_progres" , "В процесі"),
        ("Done" , "Виконано"),
    ]

    name = models.CharField(max_length=100, verbose_name="Назва задачі")
    description = models.TextField(blank=True, null=True, verbose_name="Опис")
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, default="Low", verbose_name="Пріорітет")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="Pending", verbose_name="Статус")
    deadline = models.DateTimeField(null=True, blank=True, verbose_name="Термін виконання")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Коли створенно")
    file = models.FileField(upload_to="task_files/", null=True, blank=True, verbose_name="Файл")
    def __str__(self):
        return f"{self.name} {self.status} {self.priority}"
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Задачі")
    content = models.TextField(verbose_name="Опис")
    file = models.FileField(upload_to="comment_files/", null=True, blank=True, verbose_name="Файл")
    def __str__(self):
        return f"{self.user} {self.task}"