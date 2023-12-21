from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Task
        
        fields = ['id', 'project', 'name', 'description', 'user', 'created_at', 
                  'due_date', 'state']