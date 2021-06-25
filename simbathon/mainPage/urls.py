from django.urls import path
from . import views

app_name = "mainPage"
urlpatterns = [
    #path('', main, name="main"),
    path('', views.ShowLecture.as_view(), name="main"),
]