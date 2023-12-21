from django.db import models
from project.models import Project
from user.models import User

# Create your models here.
class Task(models.Model):
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    state = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name