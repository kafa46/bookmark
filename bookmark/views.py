from django.shortcuts import render

# Create your views here.
# 어느 회사를 가든 CRUD 능력을 먼저 본다
# CRUD가 되면 일을 할 수 있다. 없으면 짤림? ^^
# CRUD: Create, Read, Update, Delete

# List
'''
웹페이지에 접속한다 -> 페이지를 요청한다(본다)
URL 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다 -> 응답한다
웹 서버가 동작할 뷰를 찾기 위해서는 해당 URL이 지정되어야 함
지정하는 역할을 하는 것 == config/urls.py에 등록하는 것 
'''

'''
뷰의 종류
    1. 클래스형 뷰
        장고에서 자주 사용하는 뷰를 미리 만들어 놓은 것
        상속받아서 쓰기 때문에 제네릭뷰(Generic View)라고 함
        빠르고 편리하게 사용할 수 있음(미리 준비된 강력함을 활용하자)

        부모 클래스 내용을 보려면, 클래스 이름 -> 우클릭 -> Go to Definition

    2. 함수형 뷰
        사용자가 목적에 맞게 만드는 뷰    
'''

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Bookmark
from django.urls import reverse_lazy

class BookmarkListView(ListView):
    # 클래스 뷰에는 반드시 모델이 들어간다
    # CRUD형 뷰에서 해당, 단순히 보여주는 뷰는 불필요함.
    model = Bookmark

class BookmarkCreateView(CreateView):
    
    # 클래스(제네릭) 뷰에는 반드시 모델이 들어간다
    # CRUD 형태의 뷰에서는 반드시 필요
    model = Bookmark
    
    # 해당 모델에 있는 것들 중에서 어떤 것을 입력하거나 수정할 것인가?
    # 해당 필드를 설정하지 않을 경우 아래와 같은 에러 발생
    #   ImproperlyConfigured at /bookmark/add/
    #   Using ModelFormMixin (base class of BookmarkCreateView) without the 'fields' attribute is prohibited.
    fields = ['site_name', 'url']

    # 다음과 같은 에러가 발생하는 경우
    #   TemplateDoesNotExist at /bookmark/add/
    #   bookmark/bookmark_form.html
    # 기본적으로 _form 접미사가 자동으로 html 이름에 부여
    # 별도 파일을 만들 경우 html 접미사를 별도로 지정해야 함.
    template_name_suffix = '_create'

    # form 입력이 완료될 경우 보여줄 페이지
    #   ImproperlyConfigured at /bookmark/update/7/1
    #   No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.
    # urls.py에 설정된 주소 중에서 원하는 경로의 name을 선택
    success_url = reverse_lazy('list')

class BookmarkDetailView(DetailView):
    # 세부 내용을 보여주는 뷰 이므로
    # 모델을 연결하는 것 이외에 특별히 설정할 것은 없음 
    # 뷰를 만들었다면 -> urls.py 설정을 통해 뷰를 연결해준다
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields =  ['site_name', 'url']
    template_name_suffix = '_update'

    # 업데이트 종료 후 에러 발생
    #   ImproperlyConfigured at /bookmark/update/7/1
    #   No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.
    
    # url을 직접 지정하는 경우(provide a url): urls.py에 설정된 주소 중에서 원하는 경로의 name을 선택
    #   클래스형 뷰: success_url 변수에 reverse_lazy를 호출하여 사용
    #   함수형 뷰: success_url 변수에 reverse를 호출하여 사용
    
    # 절대경로를 지정하는 경우(define a get_absolute_url method on the Model)
    #   모델에서 get_absolute_url method를 지정
    #   get_absolute_url은 객체의 상세 화면 주소를 반환
    #   만약 모델에서 get_absolute_url를 정의한다면 revers_lazy를 이용하여 
    #   success_url을 지정하지 않아도 됨


class BookmarkDeleteView(DeleteView):
    # 클래스(제네릭) 뷰에는 반드시 모델이 들어간다
    # CRUD 형태의 뷰에서는 반드시 필요
    model = Bookmark

    # 삭제하고 나면 어디론가 이동해서 보여줘야 함
    # 따라서 success_url이 필요함
    # 삭제하면 해당 정보가 사라지므로,
    # 해당 인스턴스의 주소를 자동으로 생성해 주는 
    # get_absolute_url은 사용할 수 없음

    success_url = reverse_lazy('list')

    # 클래스(제네릭) 뷰에서 reverse_lazy을 사용하는 이유?
    # Django는 라우팅 테이블이 불러지지 않은 상태에서
    # 클래스 뷰를 먼저 점검하게 됨
    # 먼저 점검하는 과정에서 reverse 주소가 없을 경우 오류 발생
    # 클래스 뷰를 가장 나중에 점검하여 주소 오류를 예방하기 위해
    # 제네릭 뷰에서는 항상 reverse_lazy를 사용함

    # -> 뷰를 완성하면, 항상 urls.py로 가서 해당 뷰를 연결해 준다
    # -> urls.py와 뷰를 연결하면 템플릿을 점검한다
    # 삭제하면 리스트를 보여줄 것이므로 bookmark_list.html 파일을 수정한다
