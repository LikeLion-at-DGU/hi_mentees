from django.shortcuts import render,redirect,get_object_or_404
from django.utils.datetime_safe import datetime
from django.db.models import Q
from question.models import UserQuestion
from review.models import Review
from .models import *
import sys
sys.path.append("..")
from accounts.models import UserProfile
from lecture.models import Lecture
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def mypage(request):
    email = request.user.email
    profiles = UserProfile.objects.get(email = email)
    return render(request, 'myPage/myPageMain.html', {'profiles':profiles})
# 개인정보 불러오는 함수
def profile(request):
    check = request.user.email
    profiles = UserProfile.objects.get(email = check)
    return render(request,'myPage/myPageProfile.html', {'profiles': profiles})

# qna 페이지로 이동하는 함수
def qna(request):
    user = request.user
    qnas = UserQuestion.objects.filter(user=user).order_by('id')
    check = request.user.email
    profiles = UserProfile.objects.get(email=check)
    page = int(request.GET.get('p', 1))
    paginator = Paginator(qnas, 6)
    boards = paginator.get_page(page)
    return render(request, 'myPage/myPageQ&A.html', {'qnas': qnas, 'profiles': profiles, 'boards': boards})

# qna 내용 작성하는 페이지로 이동하는 함수
def new_qna(request):
    check = request.user.email
    profiles = UserProfile.objects.get(email=check)
    lecture_list = Lecture.objects.filter(enrol_students__email=check)
    return render(request, 'myPage/new_qna.html', {'profiles': profiles, 'lecture_list': lecture_list})

# qna 작성 데이터를 저장하는 함수
def create_qna(request):
    new_qna = UserQuestion()
    new_qna.title = request.POST['title']
    new_qna.user = request.user
    new_qna.question_reg_date = timezone.now()
    new_qna.category = request.POST['category_radio']
    lectureID = request.POST['lecture_select2']
    lectureIDGet = Lecture.objects.get(id=lectureID)
    new_qna.lecture = lectureIDGet
    new_qna.content = request.POST['content']
    new_qna.save()
    return redirect('myPage:qna')

#강사진/강의 후기 페이지로 이동하는 함수
def review (request):
    user = request.user
    reviews = Review.objects.filter(user=user)
    check = request.user.email
    profiles = UserProfile.objects.get(email=check)
    page = int(request.GET.get('p',1))
    paginator = Paginator(reviews,6)
    boards = paginator.get_page(page)
    return render(request, 'myPage/myPageReview.html', {'reviews':reviews,'profiles':profiles, 'boards':boards})

#강사진/강의 후기 작성하는 페이지로 이동하는 함수
def new_review(request):
    check = request.user.email
    profiles = UserProfile.objects.get(email = check)
    lecture_list = Lecture.objects.filter(enrol_students__email=check, app_end_date__lt=datetime.now())
    host = UserProfile.objects.filter(job = '강사')
    return render(request, 'myPage/new_review.html', {'profiles': profiles, 'lecture_list': lecture_list, 'host':host})


#강사진/강의 후기 작성하는 페이지로 이동하는 함수
def new_review_lecture(request):
    check = request.user.email
    profiles = UserProfile.objects.get(email = check)
    lecture_list = Lecture.objects.filter(enrol_students__email=check, app_end_date__lt=datetime.now())
    return render(request, 'myPage/new_review_lecture.html', {'profiles': profiles, 'lecture_list': lecture_list})

#강사진/강의 후기 생성 함수
def create_review(request):
    new_review = Review()
    new_review.category = request.POST['category']
    lectureID = request.POST['lecture_select2']
    lectureIDGet = Lecture.objects.get(id=lectureID)
    new_review.lecture = lectureIDGet
    if request.POST['category']=="강의리뷰":
        new_review.teacher = None
    else:
        teacherID = request.POST['teacher_select']
        teacherIDGet = UserProfile.objects.get(id=teacherID)
        new_review.teacher = teacherIDGet
    new_review.user = request.user
    new_review.content = request.POST['content']
    new_review.review_reg_date = timezone.now()
    new_review.save()
    return redirect('myPage:review')

# (학생)신청강의 목록 페이지 나오게 하기
def enrol_list(request):
    user = request.user
    now=datetime.now()
    lectures = Lecture.objects.filter(~Q(app_end_date__lte=now), enrol_students__in = [user]).order_by('app_end_date')
    page = int(request.GET.get('p',1))
    paginator = Paginator(lectures,3)
    boards = paginator.get_page(page)
    return render(request, 'myPage/enrol_list.html', {'enrol':enrol_list, 'lectures':lectures, 'boards':boards})

# (학생)수강한 강의목록 페이지 나오게 하기
def finish_list(request):
    user = request.user
    now=datetime.now()
    lectures = Lecture.objects.filter(app_end_date__lte=now, enrol_students__in = [user]).order_by('-app_end_date')
    page = int(request.GET.get('p',1))
    paginator = Paginator(lectures,3)
    boards = paginator.get_page(page)
    return render(request, 'myPage/finish_list.html', {'lectures':lectures, 'boards':boards})

# (강사)강의한 강의목록 페이지 나오게 하기
def lectured_list(request):
    email = request.user.email
    teacher = UserProfile.objects.get(email = email)
    now=datetime.now()
    lectures = Lecture.objects.filter(app_end_date__lte=now, host__in =[teacher]).order_by('-app_end_date')
    page = int(request.GET.get('p',1))
    paginator = Paginator(lectures,3)
    boards = paginator.get_page(page)
    teacher.service_hour = 0
    for i in lectures:
        teacher.service_hour += i.lec_time
    teacher.save()
    return render(request, 'myPage/lectured_list.html', {'lectures':lectures, 'boards':boards})    