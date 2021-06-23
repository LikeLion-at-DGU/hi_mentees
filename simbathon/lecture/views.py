from .models import Lecture
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    lectures=Lecture.objects.all()
    return render(request, 'lecture/lectureMain.html',{'lectures':lectures})

def detail(request, id):
    lecture=get_object_or_404(Lecture, pk=id)
    return render(request, 'lecture/lectureDetail.html',{'lecture':lecture})

@login_required
def enrol_student(request, lecture_id):
    lecture=get_object_or_404(Lecture, id=lecture_id) 
    lecture.enrol_students.add(request.user)