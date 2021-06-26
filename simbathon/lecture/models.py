from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
import sys
sys.path.append("..")
from accounts.models import UserProfile
from django.conf import settings

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.name

#카테고리 


class Lecture(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    #제목
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    #주제
    body=models.TextField()
    #내용
    LEVEL_CHOICE = (
    ('star1','1단계'),
    ('star2','2단계'),
    ('star3','3단계'),
    ('star4','4단계'),
    ('star5','5단계'),)
    level=models.CharField(max_length=10, choices=LEVEL_CHOICE)
    #난이도
    host=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    #강사진 #강의:강사=1:n모델
    app_start_date=models.DateTimeField()
    #강의신청 시작일
    app_end_date=models.DateTimeField()
    #강의신청 마감일
    thumbnail=models.ImageField(upload_to='images/',blank=True, null=True)
    #강의 썸네일
    lec_time=models.IntegerField(default=0)
    schedule=models.ImageField(upload_to='images/',blank=True, null=True)
    #시간표
    enrol_students=models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="enrol")
    #좋아요한 사용자
    like_users=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_lectures")
    def __str__(self):
        return self.title #입력한 데이터가 호출되면 제목이 대표값으로 나오게 한다.

    def summary(self):
        return self.body[:20]

    class Meta:
        db_table='Lecture'

