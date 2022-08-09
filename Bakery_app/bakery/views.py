from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .serializers import IngredientSerializer, UserSerializer, LoginSerializer
from .models import Ingredient, Item, LoginUser, Requirements


from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response


class UserSignUp(APIView):

    def get(self, request):
        userdetails = User.objects.all()
        print(userdetails)
        serializer = UserSerializer(userdetails, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'serializer':'Invalid data'}, status= status.HTTP_400_BAD_REQUEST)


class UserLogIn(APIView):
    @csrf_exempt
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        x = authenticate(request, username=username, password=password)
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            if x is not None:
                login(request, x)
                return Response({"user": "Logged in"}, status=status.HTTP_200_OK)
            else:
                return Response({"Credentials": "invalid"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Serializer": "invalid"}, status=status.HTTP_404_NOT_FOUND)


class ingredient_list(APIView):
    def get(self, request):
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'items':'Here is the list!'}, status=status.HTTP_201_CREATED)
        return Response({'List':'Not Valid'}, status=status.HTTP_400_BAD_REQUEST)


def calculate(request):
    item = Item.objects.all()
    require_item = Requirements.objects.filter(item_name=item[0].item_name)
    return HttpResponse(require_item)
















# Create your views here.
