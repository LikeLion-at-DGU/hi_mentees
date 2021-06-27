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
    path('new_review_lecture/',views.new_review_lecture, name="new_review_lecture"),
    path('create_review',views.create_review, name="create_review"),
]