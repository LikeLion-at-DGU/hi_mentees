from django.conf import settings
from django.db import models
from django.utils import timezone
from accounts.models import UserProfile
from lecture.models import Lecture


class Review(models.Model):
    category_choice = (
        ('강사리뷰', '강사리뷰'),
        ('강의리뷰', '강의리뷰'),
    )
    category = models.CharField(max_length=10, choices=category_choice)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    review_reg_date = models.DateTimeField(default=timezone.now, verbose_name="리뷰작성일")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, verbose_name="질문자")

