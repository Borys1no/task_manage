from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('in_progress', 'En progreso'),
        ('donde', 'Completada'),
    ]

    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    description = models.TextField(blank= True)
    status = models.CharField(
        max_length=20,
        choices= STATUS_CHOICES,
        default= 'pending'
    )
    user= models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self)-> str:
        return str (self.title)
    