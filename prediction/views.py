from django.shortcuts import render
from .models import DiabetesResult

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def prediction_service(request):
  return render(request, 'prediction/prediction_service.html')

def result(request):

  data = pd.read_csv(r'C:\Users\HORIZON\Downloads\Work\django\uni\new\prediction\diabetes.csv')
  x = data.drop('Outcome', axis=1)
  y = data['Outcome']
  X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.30)
  
  model = LogisticRegression() 
  model.fit(X_train,y_train)
  
  val1 = float(request.GET['n1'])
  val2 = float(request.GET['n2'])
  val3 = float(request.GET['n3'])
  val4 = float(request.GET['n4'])
  val5 = float(request.GET['n5'])
  val6 = float(request.GET['n6'])
  val7 = float(request.GET['n7'])
  
  
  predictions = model.predict([[val1, val2, val3, val4, val5, val6, val7]])
  
  result1 = ""
  if predictions==[1]:
    result1="Positive"
  else:
    result1="negative"
    
  # Fetch user and create a DiabetesResult object with all necessary fields
    user = request.user

    # Create a DiabetesResult instance with age included
    result_instance = DiabetesResult(
        user=user,
        result=result1,
        age=val7,  # Add the age field
        blood_pressure=val2,
        bmi=val5,
        skin_thickness=val3,
        diabetes_pedigree_function=val6,
        glucose=val1,
        insulin=val4
    )
  result_instance.save()

  
  return render(request, 'prediction/prediction_service.html',{"result2":result1})


def user_results(request):
    user = request.user
    results = DiabetesResult.objects.filter(user=user).order_by('-date_created')
    return render(request, 'prediction/user_results.html', {"results": results})
  
  