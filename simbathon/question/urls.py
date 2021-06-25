from django.urls import path
from . import views

app_name = "question"

urlpatterns = [
    path('index/', views.QuestionList.as_view(), name="index"),
    path('index/result', views.result, name="result"),
]