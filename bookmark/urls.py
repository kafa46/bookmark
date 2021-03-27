from django.urls import path
from .views import *

# urlpattern 사용법
#   path('패스 이름', view 이름, 해당 패턴의 이름(템플릿에서 활용))

# 클래스 뷰를 사용할 경우 반드시 .as_view() 사용
# 클래스 뷰를 함수형 뷰로 바꿔주는 메소드
# Django의 경우 기본적으로 모든 뷰는 함수형으로 작동

urlpatterns = [
    # http://127.0.0.1/bookmark/
    # 템플릿을 작성하지 않았다면, http://127.0.0.1/bookmark/ 접속해도 오류 -> 정상 상황
    # 보여줄 html이 없으므로 당연히 TemplateDoesNotExist 에러 발생
    # 다음 순서로 템플릿 작성하면 됨
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    
    # int: converter 혹은 validator라고 부름. 해당되는 형태가 오면 허용
    # pk: 정수형이 맞다면, model에서 pk(primary key)를 url 주소 지정
    # slug 형태: (예) thewordcracker.com -> 검색엔진 SEO를 위해 사용
    # 접근 url 형태 -> http://127.0.0.1:8000/bookmark/detail/1/
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),

    # -> urls.py에서 해당 view를 연결해 주고나서 템플릿을 점검한다
]

