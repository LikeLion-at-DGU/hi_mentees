from .models import Lecture
from django.shortcuts import render,get_object_or_404

def index(request):
    lectures=Lecture.objects.all()
    return render(request, 'lecture/lectureMain.html',{'lectures':lectures})

def detail(request, id):
    lecture=get_object_or_404(Lecture, pk=id)
    return render(request, 'lecture/lectureDetail.html',{'lecture':lecture})

