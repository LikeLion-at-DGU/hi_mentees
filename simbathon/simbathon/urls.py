from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('mainPage.urls')),
    path('lecture/', include('lecture.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
