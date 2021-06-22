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

    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':''}))
    job = forms.ChoiceField(choices= JOB_CHOICE)
    school = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'ex)동국대학교'}))
    grade = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'ex)중학교 1학년'}))
    interests = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':''}))

    def signup(self, request, user):
        userProfile = UserProfile()
        userProfile.user = user
        userProfile.name = self.cleaned_data[('name')]
        userProfile.job = self.cleaned_data[('job')]
        userProfile.email = user.email
        userProfile.school = self.cleaned_data[('school')]
        userProfile.grade = self.cleaned_data[('grade')]
        userProfile.interests = self.cleaned_data[('interests')]
        userProfile.save()
        user.save()
        return user