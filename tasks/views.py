from django.shortcuts import render
from rest_framework.views import APIView
from .models import Task
from project.models import Project
from user.models import User
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.
class CreateTaskView(APIView):
    def post(self, request):
        
        # get data #
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # get project object #
        project_name = serializer.validated_data.get('project')
        project = Project.objects.get(name=project_name)
        
        if project:
            # get user object #
            user_e = serializer.validated_data.get('user')
            user = User.objects.get(email=user_e)
            if user:
                serializer.save()
                return Response(serializer.data)

        
# View information about Project #     
class TaskView(generics.ListAPIView):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
# View each Project #    
class EachTaskView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer