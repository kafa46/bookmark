"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 슬래시(/)를 빼먹지 말자!
urlpatterns = [
    # 1차 url -> 2차 -> 3차 ...
    # 대학병원 접수 -> 해당 진료과 데스크 -> 의사선생님 방
    
    path('admin/', admin.site.urls),
    
    # 1차: http:127.0.0.1/bookmark
    path('bookmark/', include('bookmark.urls')),

    # 해당 앱 폴더 안에 url.py를 만들어서 설정
    # 2차: http:127.0.0.1/bookmark/xxx
]
