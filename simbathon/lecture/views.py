from .models import Lecture
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required


def index(request):
    lectures=Lecture.objects.all()
    return render(request, 'lecture/lectureMain.html',{'lectures':lectures})

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
   
