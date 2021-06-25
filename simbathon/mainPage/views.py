from django.shortcuts import render
# from .models import Lecture
from django.shortcuts import render,get_object_or_404

def main(request):
    return render(request, 'mainPage/mainPage.html')

