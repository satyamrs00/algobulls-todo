from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

STATUS_CHOICES = [ (0, 'OPEN'), (1, 'WORKING'), (2, 'DONE'), (3, 'OVERDUE') ]
class User(AbstractUser):
    pass

class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    due_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name