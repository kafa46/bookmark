from django.contrib import admin

# Register your models here.
# 내가 만든 모델을 관리자 페이지에서 관리할 수 있도록 등록하는 파일

from .models import Bookmark

admin.site.register(Bookmark)