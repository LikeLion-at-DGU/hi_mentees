from django.shortcuts import render,redirect,get_object_or_404
from django.utils.datetime_safe import datetime

from lecture.models import Lecture
from question.models import UserQuestion
from review.models import Review
from .models import *
import sys
sys.path.append("..")
from accounts.models import UserProfile
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
    profiles = UserProfile.objects.get(email = check)
    page = int(request.GET.get('p',1))
    paginator = Paginator(qnas,6)
    boards = paginator.get_page(page)
    return render(request, 'myPage/myPageQ&A.html', {'qnas':qnas,'profiles':profiles, 'boards':boards})


# qna 내용 작성하는 페이지로 이동하는 함수
def new_qna(request):
    check = request.user.email
    profiles = UserProfile.objects.get(email=check)
    lecture_list = Lecture.objects.filter(enrol_students__email=check)
    return render(request, 'myPage/new_qna.html', {'profiles': profiles, 'lecture_list': lecture_list})


# qna 내용 읽어오는 함수
def detail_qna(request,id):
    qna = get_object_or_404(UserQuestion, pk=id)
    check = request.user.email
    profiles = UserProfile.objects.get(email=check)
    return render(request, 'myPage/detail_qna.html', {'qna': qna, 'profiles': profiles})


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
    return redirect('myPage:detail_qna', new_qna.id)


# qna 수정본 작성 페이지 호출하는 함수
def edit_qna(request, id):
    qna = QnA.objects.get(id = id)
    check = request.user.email
    profiles = UserProfile.objects.get(email = check)
    return render(request, 'myPage/edit_qna.html', {'qna':qna, 'profiles':profiles})

# qna 수정후 데이터 베이스 저장 및 변화된 글 나오게 하는 함수
def update_qna(request, id):
    update_qna = QnA.objects.get(id = id)
    update_qna.title = request.POST['title']
    update_qna.writer = request.user
    update_qna.pub_date = timezone.now()
    update_qna.body = request.POST['body']
    update_qna.save()
    return redirect('myPage:detail_qna', update_qna.id)
# qna 삭제 후 qna 목록으로 이동하는 함수
def delete_qna(request,id):
    delete_qna = QnA.objects.get(id = id)
    delete_qna.delete()
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
    return render(request, 'myPage/new_review.html', {'profiles': profiles})
#강사진/강의 후기 작성내용 보는 페이지
def detail_review(request,id):
    review = get_object_or_404(Reviews, pk = id)
    check = request.user.email
    profiles = UserProfile.objects.get(email = check)
    return render(request, 'myPage/detail_review.html', {'review' : review, 'profiles':profiles})
#강사진/강의 후기 생성 함수
def create_review(request):
    new_review = Reviews()
    new_review.title = request.POST['title']
    new_review.writer = request.user
    new_review.pub_date = timezone.now()
    new_review.body = request.POST['body']
    new_review.image = request.FILES.get('image')
    new_review.save()
    return redirect('myPage:detail_review', new_review.id)
# 강사진/강의 후기 수정본 작성 페이지 호출하는 함수
def edit_review(request, id):
    review = Reviews.objects.get(id = id)
    check = request.user.email
    profiles = UserProfile.objects.get(email = check)
    return render(request, 'myPage/edit_review.html', {'review':review, 'profiles':profiles})
# qna 수정후 데이터 베이스 저장 및 변화된 글 나오게 하는 함수
def update_review(request, id):
    update_review = Reviews.objects.get(id = id)
    update_review.title = request.POST['title']
    update_review.writer = request.user
    update_review.pub_date = timezone.now()
    update_review.body = request.POST['body']
    update_review.save()
    return redirect('myPage:detail_review', update_review.id)

def delete_review(request,id):
    delete_review = Reviews.objects.get(id = id)
    delete_review.delete()
    return redirect('myPage:review')