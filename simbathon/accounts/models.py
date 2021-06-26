from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    JOB_CHOICE = (
        ('학생', '학생'),
        ('강사', '강사'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(max_length=20,default='')
    job = models.CharField(max_length=2, choices= JOB_CHOICE)
    school = models.CharField(max_length=30, default='')
    grade = models.CharField(max_length=30, default='')
    school_id = models.CharField(max_length=30,default='')
    interests = models.CharField(max_length=30,default='')
    service_hour = models.ImageField(default=0)
    webex = models.URLField(max_length=100, default='')
    admin_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']
        db_table = 'user_profile'

        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profile'

    def __str__(self):
        return self.name
   