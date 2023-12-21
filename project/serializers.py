from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Project # model
        
        fields = ['id', 'name', 'description', 'user_manage', 'created_at'] # field
    
