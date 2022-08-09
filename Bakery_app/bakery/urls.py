from django.urls import path, include
from .models import Ingredient
from .views import ingredient_list, UserSignUp, UserLogIn

urlpatterns= [
    path('ingredients/',ingredient_list.as_view()),
    path('signup/', UserSignUp.as_view()),
    path('login/', UserLogIn.as_view()),

]