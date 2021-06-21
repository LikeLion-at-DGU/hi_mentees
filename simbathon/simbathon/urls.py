from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('mainPage.urls')),
    path('lecture/', include('lecture.urls')),
    path('accounts/',include('allauth.urls')),
]
