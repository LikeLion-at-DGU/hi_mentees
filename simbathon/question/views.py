from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import UserQuestion


class QuestionList(ListView):
    # 어떤 테이블에서 객체 리스트를 가져올 것인지 지정해주기
    model = UserQuestion
    # 템플릿 파일로 넘겨주는 객체 리스트의 이름 지정
    context_object_name = 'question_list'
    # 템플릿 파일 위치 지정
    template_name = 'question/question_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # 선택된 대분류의 상품 목록
        context['about_lecture'] = UserQuestion.objects.exclude(answer__exact='').filter(category='학습내용')
        context['about_hisw'] = UserQuestion.objects.exclude(answer__exact='').filter(category='hi-sw 관련')
        context['about_school'] = UserQuestion.objects.exclude(answer__exact='').filter(category='진학상담')
        context['about_etc'] = UserQuestion.objects.exclude(answer__exact='').filter(category='기타')
        return context

def result(request):
	query = request.GET['query']
	if query:
		query_lecture = UserQuestion.objects.exclude(answer__exact='').filter(category='학습내용', lecture__title__contains=query)
	return render(request, 'question/question_list.html', {'about_lecture': query_lecture})
