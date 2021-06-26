from django.contrib import admin
from .models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'job', 'email', 'school', 'grade', 'school_id', 'interests', 'service_hour', 'admin_approved')
    list_filter= ['admin_approved', 'job']
admin.site.register(UserProfile, UserProfileAdmin)