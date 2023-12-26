from django.contrib import admin
from django.urls import path, include 
from django.views.generic import TemplateView
from .views import prediction_service

urlpatterns = [
    path('prediction-service/', prediction_service, name='prediction_service'),
]
