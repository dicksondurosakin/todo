from time import timezone
from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=400)
    date_added = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ['-date_added']