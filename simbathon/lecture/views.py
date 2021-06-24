from .models import Lecture
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime

def index(request):
    now=datetime.now()
    ing_lectures=Lecture.objects.filter(app_end_date__gte=now,app_start_date__lte=now)
    expected_lectures=Lecture.objects.filter(app_start_date__gte=now)
    return render(request, 'lecture/lectureMain.html',{'ing_lectures':ing_lectures, 'expected_lectures':expected_lectures})

def detail(request, id):
    lecture=get_object_or_404(Lecture, pk=id)
    return render(request, 'lecture/lectureDetail.html',{'lecture':lecture})

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
    return render(request, 'lecture/lectureMain.html',{'lectures':lectures})
   

