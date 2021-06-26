from django.shortcuts import render
from django.views.generic import ListView, DetailView
import sys
sys.path.append("..")
from lecture.models import Lecture


class ShowLecture(ListView):
    # 어떤 테이블에서 객체 리스트를 가져올 것인지 지정해주기
    model = Lecture
    # 템플릿 파일로 넘겨주는 객체 리스트의 이름 지정
    context_object_name = 'lecture_list'
    # 템플릿 파일 위치 지정
    template_name = 'mainPage/mainPage.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # 선택된 대분류의 상품 목록
        
        context['about_alllecture'] = Lecture.objects.all()
        context['about_popularlecture'] = Lecture.objects.filter( showmain_lecture='인기강의')
        context['about_upcominglecture'] = Lecture.objects.filter(showmain_lecture ='일주일 내 시작될 강의')

        print(context)
        return context
    

