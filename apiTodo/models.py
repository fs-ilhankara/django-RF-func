from django.db import models
from django.db.models.fields import DateTimeField, TextField

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)

    TITLE = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low')
    )
    priority = models.CharField(max_length=50, choices=TITLE, default='L')

    done = models.BooleanField(default=False)

    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
