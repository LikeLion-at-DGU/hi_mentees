from django.views.generic.list import ListView
from .models import  Lecture
from django.shortcuts import render,get_object_or_404,redirect,get_list_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime


class LectureList(ListView):
    model=Lecture
    context_object_name="lecture_list"
    template_name='lecture/lectureMain.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        now=datetime.now()
        context['ing_all']=Lecture.objects.all().filter(app_end_date__gte=now,app_start_date__lte=now)
        context['expected_all']=Lecture.objects.filter(app_start_date__gte=now)
        context['ing_python']=Lecture.objects.filter(category='python', app_end_date__gte=now,app_start_date__lte=now)
        context['expected_python']=Lecture.objects.filter(category='python',app_start_date__gte=now)
        context['ing_ozobot']=Lecture.objects.filter(category='ozobot', app_end_date__gte=now,app_start_date__lte=now)
        context['expected_ozobot']=Lecture.objects.filter(category='ozobot',app_start_date__gte=now)
        context['ing_entry']=Lecture.objects.filter(category='entry', app_end_date__gte=now,app_start_date__lte=now)
        context['expected_entry']=Lecture.objects.filter(category='entry',app_start_date__gte=now)
        context['ing_goorum']=Lecture.objects.filter(category='goorum', app_end_date__gte=now,app_start_date__lte=now)
        context['expected_goorum']=Lecture.objects.filter(category='goorum',app_start_date__gte=now)
        context['ing_etc']=Lecture.objects.filter(category='etc', app_end_date__gte=now,app_start_date__lte=now)
        context['expected_etc']=Lecture.objects.filter(category='etc',app_start_date__gte=now)
        return context




def detail(request, id):
    lecture=get_object_or_404(Lecture, pk=id)
    return render(request, 'lecture/lectureDetail.html',{'lecture':lecture})

def detail2(request,id): #아직 신청기간 아닌 강의의 detail을 보여주는 함수
    lecture=get_object_or_404(Lecture, pk=id)
    return render(request, 'lecture/lectureDetail2.html',{'lecture':lecture})

def enrol_student(request, id):
    lecture=get_object_or_404(Lecture, pk=id) 
    lecture.enrol_students.add(request.user)
    lecture.save()
    return render(request, 'lecture/lectureDetail.html',{'lecture':lecture})
    

def drop_student(request, id):
    lecture=get_object_or_404(Lecture, pk=id)
    lecture.enrol_students.remove(request.user)
    lecture.save()
    lectures=Lecture.objects.all()
    return render(request, 'lecture/lectureDetail.html',{'lecture':lecture})
    
   
def like(request, pk):
    lecture=get_object_or_404(Lecture, pk=pk)
    if request.user in lecture.like_users.all():
        lecture.like_users.remove(request.user)
    else:
        lecture.like_users.add(request.user)
    return redirect('lecture:detail', lecture.id)
