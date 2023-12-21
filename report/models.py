from django.db import models
from project.models import Project
from user.models import User

# Create your models here.
class Report(models.Model):
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    performance = models.PositiveIntegerField(blank=True)
    
    def __str__(self):
        return self.project.name
    
class EmployeePerform(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tasks_complete = models.PositiveIntegerField(blank=True)
    
    
    def __str__(self):
        return self.user.name
