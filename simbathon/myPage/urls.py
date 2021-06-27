from django.urls import path
from . import views

app_name = "myPage"
urlpatterns = [
    path('', views.mypage, name= "mypage"),
    path('Profile/', views.profile, name = "profile"),
    path('qna/', views.qna, name="qna"),
    path('new_qna/', views.new_qna, name="new_qna"),
    path('create_qna/',views.create_qna, name="create_qna"),
    path('review/',views.review, name="review"),
    path('new_review/',views.new_review, name="new_review"),
    path('new_review_lecture/',views.new_review_lecture, name="new_review_lecture"),
    path('create_review',views.create_review, name="create_review"),
    path('enrol_list/' , views.enrol_list, name="enrol_list"),
    path('finish_list/',views.finish_list, name="finish_list"),
    path('lectured_list/', views.lectured_list, name="lectured_list"),
]