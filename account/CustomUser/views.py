from django.shortcuts import render
from rest_framework.generics import GenericAPIView
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .serializers import SignUpSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

from rest_framework.views import APIView

@api_view(['POST'])
def login_user(request):
    username = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        return Response({'access_token': access_token}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

'''
@api_view(['POST'])
def login_user(request):
    username = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        return Response({'access_token': access_token}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

'''

'''
class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User signup successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
class SignUpView(GenericAPIView):
    serializer_class =SignUpSerializer
    permission_classes=[]

    def post(self, request:Request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response={
                'message':"User signup successfully",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

    

class LoginView(APIView):
    permission_classes=[]
    def post(self, request:Request):
        email= request.data.get('email')
        password= request.data.get('password')

        user= authenticate(email=email, password=password)
        if user is not None:
            response={
                "message":"login successfully",
                "token":user.auth_token.key
            }
            return Response(data=response,status=status.HTTP_200_OK)
        else:
            return Response(data={"message":'invalid email or password'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request:Request):
        cotent={
            "user":str(request.user),
            "auth":str(request.auth)
        }
        return Response(data=cotent, status=status)