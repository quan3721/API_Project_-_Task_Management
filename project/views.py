from django.shortcuts import render

# Create your views here
from rest_framework.views import APIView
from rest_framework import generics
from .models import Project
from user.models import User
from .serializers import ProjectSerializer
from rest_framework.response import Response


# Create a new Project # 
class PostProjectView(APIView):
    def post(self, request):
        # get data #
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_manage = serializer.validated_data.get('user_manage')
        user = User.objects.get(email=user_manage)
        
        if user.role == 'manager': 
            serializer.save()
            return Response(serializer.data)
        else:
            response = Response()
            response.data = {
                'message': 'User is not manager'
            }
            return response

# View information about Project #
class ProjectView(generics.ListAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
        
# View each Project #
class EachProjectView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
        

    