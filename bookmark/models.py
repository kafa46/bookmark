from django.db import models

# 모델 안에서 reverse 사용
# 클래스형 뷰에서는 reverse_lazy 사용
from django.urls import reverse

# Create your models here.

# 모델을 만든다: 데이터베이스를 객체로 만들어 사용하겠다.
# 모델: 테이블
# 모델의 필드: 테이블의 컬럼(열)
# 인스턴스: 테이블의 레코드(행)
# 필드의 값(인스턴스의 필드값): 레코드의 컬럼 데이터 값 

# 데이터베이스에 무엇인가 저장하고 싶을 경우에는 모델을 만든다!
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL') # CharField를 써도 됨

    ''' 
    필드의 종류가 결정하는 것
        1. 데이터베이스의 컬럼 종류
        2. 각 종 제약사항(글자수 등)
        3. Form의 종류를 결정
        4. Form에서의 제약 사항
    
    모델을 만들었다는 의미 -> 어떤 형태로 넣을지 결정
    
    모델을 만든 이후에 할 일
    makemigrations -> 모델의 변경사항을 추적하여 기록해 놓는 일(파일로 자동 생성됨)
    migration -> 데이터베이스에 모델의 내용을 반영(테이블 생성)

    모델이 잘 생성되었는지 확인하는 방법
    admin.py에 모델을 등록하고,
    서버를 실행하여 admin page를 확인한다.
    '''

    # admin page instance 출력 시 보기 좋게 하기 위하여
    # __str__ 변경
    def __str__(self):
        return '이름: {},  주소: {}'.format(self.site_name, self.url)

    def get_absolute_url(self):
        # 데이터베이스 1건당 하나의 인스턴스 단위로 다룬다
        # 해당 인스턴스의 상세페이지를 생성하는 메서드 (django에서 제공하는 기능)

        # 해당 필드의 주소를 만들어서 리턴하는 메서드
        # 보통은 객체의 화면 상세 주소를 반환

        # 특정 모델에 대한 Detail뷰를 작성할 경우, Detail뷰에 대한 URLConf설정을 하자마자,
        # 필히 get_absolute_url설정을 해주세요. 코드가 보다 간결해집니다
        # 어떠한 모델에 대해서 detail 뷰를 만들게 되면 get_absolute_url() 멤버 함수를 무조건 선언
        # resolve_url(모델 인스턴스), redirect(모델 인스턴스) 를 통해서 
        # 모델 인스턴스의 get_absolute_url() 함수를 자동으로 호출
        # resolve_url() 함수는 가장 먼저 get_absolute_url 함수의 존재 여부를 체크하고, 
        # 존재하면 호출하며 그 리턴값으로 URL을 사용
        
        # return reverse('detail', args=[str(self.id)])
        return reverse('detail', args=[self.id])

