from django.db import models
from user.models import User

# Create your models here.
class Project(models.Model):
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    user_manage = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name