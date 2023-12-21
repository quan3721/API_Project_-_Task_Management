from django.shortcuts import render
from .serializers import ReportSerializer, EmployeePerformSerializer
from rest_framework import generics
from .models import Report
from project.models import Project
from tasks.models import Task
from rest_framework.views import APIView
from rest_framework.response import Response
from tasks.serializers import TaskSerializer
from user.models import User
# Create your views here.
class CreateReportView(APIView):
    def post(self, request):
        # get data #
        serializer = ReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # get project object #
        project_name = serializer.validated_data.get('project')
        project = Project.objects.get(name=project_name)
        
        if project:
            # get task object #
            total_task = 0
            tasks = Task.objects.filter(project=project)
            total_task = tasks.count()
                       
            count = 0
            performance = 0
            for task in tasks:
                if task.state == "Successful":
                    count += 1
            performance = (count / total_task) * 100
            
            serializer.save(project=project, performance=performance)
            
            return Response(serializer.data)
        
class ViewEmpPerformance(APIView):
    def post(self, request):
        serializer = EmployeePerformSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # get user object #
        user_email = serializer._validated_data.get('user')
        user = User.objects.get(email=user_email)
        if user:
            tasks = Task.objects.filter(user=user)
            
            count = 0
            for task in tasks:
                if task.state == "Successful":
                    count += 1
            tasks_complete = count
            
            serializer.save(user=user, tasks_complete=tasks_complete)
            return Response(serializer.data)
            
            
        

    
    
        
    
        