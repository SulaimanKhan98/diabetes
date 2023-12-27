from django.contrib import admin
from django.urls import path, include 
from django.views.generic import TemplateView
from .views import prediction_service, result, user_results

urlpatterns = [
    path('prediction-service/', prediction_service, name='prediction_service'),
    path('prediction-service/result/', result, name='prediction_result'),
     path('user-results/', user_results, name='user_results'),
     ]

