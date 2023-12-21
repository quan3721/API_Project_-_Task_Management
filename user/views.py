from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        # get data for serializer #
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) # valid data
        serializer.save() # save
        
        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        
        # find user object #
        user = User.objects.filter(email=email).first() 
        
        # check user is exist ? #
        if user is None:
            raise AuthenticationFailed('User not found!')
        
        # check password of user #
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        # data for token #
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60), # keep code token exists 60 minutes = 1 hour
            'iat': datetime.datetime.utcnow() # time created token
        }
        token = jwt.encode(payload=payload, key='secret', algorithm='HS256') # create Token code
        
        # response on cookies #
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True, secure=True)
        response.data = {
            'jwt': token
        }
        
        return response

class UserView(APIView):
    
    def get(self, request):
        
        # get token from cookies #
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed("Unauthenticated!")
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256']) # get payload data
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")
        
        # get user object #
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt') # delete cookie
        response.data = {
            'message': 'success'
        }
       
        return response