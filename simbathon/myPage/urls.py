from django.urls import path
from . import views

app_name = "myPage"
urlpatterns = [
    path('', views.mypage, name= "mypage"),
    path('Profile/', views.profile, name = "profile"),
    path('qna/', views.qna, name="qna"),
    path('new_qna/', views.new_qna, name="new_qna"),
    path('detail_qna/<str:id>',views.detail_qna, name="detail_qna"),
    path('create_qna/',views.create_qna, name="create_qna"),
    path('edit_qna/<str:id>', views.edit_qna, name="edit_qna"),
    path('update_qna/<str:id>', views.update_qna, name="update_qna"),
    path('delete_qna/<str:id>', views.delete_qna, name="delete_qna"),
    path('review/',views.review, name="review"),
    path('new_review/',views.new_review, name="new_review"),
    path('detail_review/<str:id>',views.detail_review, name="detail_review"),
    path('create_review',views.create_review, name="create_review"),
    path('edit_review/<str:id>', views.edit_review, name="edit_review"),
    path('update_review/<str:id>', views.update_review, name="update_review"),
    path('delete_review/<str:id>', views.delete_review, name="delete_review"),
    path('enrol_list/' , views.enrol_list, name="enrol_list"),
    path('finish_list/',views.finish_list, name="finish_list"),
    path('lectured_list/', views.lectured_list, name="lectured_list"),
]