from django.urls import path
from . import views

app_name = "review"

urlpatterns = [
    path('index/', views.ReviewList.as_view(), name="index"),
    path('index/result_teacher', views.result_teacher, name="result_teacher"),
    path('index/result_lecture', views.result_lecture, name="result_lecture"),
]