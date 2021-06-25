from django.conf import settings
from django.db import models
from django.utils import timezone

from accounts.models import UserProfile
from lecture.models import Lecture


class UserQuestion(models.Model):
    category_choice = (
        ('학습내용', '학습내용'),
        ('hi-sw 관련', 'hi-sw 관련'),
        ('진학상담', '진학상담'),
        ('기타', '기타'),
    )
    category = models.CharField(max_length=10, choices=category_choice, default='기타')
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    question_reg_date = models.DateTimeField(default=timezone.now, verbose_name="질문작성일")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, verbose_name="질문자")
    answer = models.TextField(verbose_name="질문에 대한 답변", null=True, blank=True)
    answer_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="질문 답변자", null=True, blank=True)
    answer_reg_date = models.DateTimeField(verbose_name="답변작성일", null=True, blank=True)
