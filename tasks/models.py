from django.db import models
from taggit.managers import TaggableManager


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    # Priorities
    PRIORITIES = [
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
    ]

    title = models.CharField(max_length=50)
    description = models.TextField()
    completed = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    priority = models.CharField(max_length=20, choices=PRIORITIES, default='high')
    due_date = models.DateField()
    
    # Tags (for categorization)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

