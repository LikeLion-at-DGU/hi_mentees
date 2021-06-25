from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


class IntroView(TemplateView):
    template_name = 'introduction.html'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainPage.urls')),
    path('main/', include('mainPage.urls')),
    path('introduction/', IntroView.as_view(), name='introduction'),
    path('lecture/', include('lecture.urls')),
    path('accounts/',include('allauth.urls')),
    path('question/', include('question.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
