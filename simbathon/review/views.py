from django.shortcuts import render
from django.views.generic import ListView
from .models import Review


class ReviewList(ListView):
    # 어떤 테이블에서 객체 리스트를 가져올 것인지 지정해주기
    model = Review
    # 템플릿 파일로 넘겨주는 객체 리스트의 이름 지정
    context_object_name = 'review_list'
    # 템플릿 파일 위치 지정
    template_name = 'review/review_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # 선택된 대분류의 상품 목록
        context['teacher_review'] = Review.objects.filter(category='강사리뷰')
        context['lecture_review'] = Review.objects.filter(category='강의리뷰')
        return context

def result_teacher(request):
	query = request.GET['query']
	if query:
		teacher_review = Review.objects.filter(teacher__name__contains=query)
	return render(request, 'review/review_list.html', {'teacher_review': teacher_review})


def result_lecture(request):
	query = request.GET['query']
	if query:
		lecture_review = Review.objects.filter(lecture__title__contains=query)
	return render(request, 'review/review_list.html', {'lecture_review': lecture_review})