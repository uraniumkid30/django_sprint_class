from django.db import models

# Create your models here.

class Book(models.Model):
    owner = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.title}"
