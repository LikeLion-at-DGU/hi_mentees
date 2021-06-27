from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import UserProfile


class SignupForm(forms.Form):
    class Meta:
        model = User
    
    JOB_CHOICE = (
        ('학생', '학생'),
        ('강사', '강사'),
    )

    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':''}),label="이름")
    job = forms.ChoiceField(choices= JOB_CHOICE, label="상태", widget=forms.Select)
    school = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'ex)동국대학교'}),label="학교")
    grade = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'ex)중학교 1학년'}),label="학년")
    school_id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':''}), label="학번")
    interests = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':''}),label="관심분야")



    def signup(self, request, user):
        userProfile = UserProfile()
        userProfile.user = user
        userProfile.name = self.cleaned_data[('name')]
        userProfile.job = self.cleaned_data[('job')]
        userProfile.email = user.email
        userProfile.school = self.cleaned_data[('school')]
        userProfile.grade = self.cleaned_data[('grade')]
        userProfile.school_id = self.cleaned_data[('school_id')]
        userProfile.interests = self.cleaned_data[('interests')]
        userProfile.save()
        user.save()
        return user