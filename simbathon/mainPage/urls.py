from django.urls import path

import sys
sys.path.append("..")
from . import views

app_name = "mainPage"
urlpatterns = [
    path('', views.ShowLecture.as_view(), name="index"),
]
