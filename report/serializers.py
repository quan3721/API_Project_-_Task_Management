from rest_framework import serializers
from .models import Report, EmployeePerform

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Report
        
        fields = ['project', 'performance']
        
class EmployeePerformSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmployeePerform
        
        fields = ['user', 'tasks_complete']
        
        