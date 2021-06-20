from django.urls import path
from .views import *

app_name = "lecture"
urlpatterns = [
    path('lecture/', index, name="index"),
    path('<str:id>',detail, name="detail"),
  
]