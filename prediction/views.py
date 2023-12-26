from django.shortcuts import render

# Create your views here.

def prediction_service(request):
  return render(request, 'prediction/prediction_service.html')