from django.urls import path
from .views import *

app_name = "lecture"
urlpatterns = [
     path('index/', LectureList.as_view(), name="index"),
    path('<str:id>',detail, name="detail"),
    path('enrol/<str:id>/',enrol_student,name='enrol_student'),
    path('drop/<str:id>/',drop_student,name="drop_student"),
    path('<int:pk>/like/',like, name='like'),
    path('<str:id>2/',detail2, name='detail2'),
]