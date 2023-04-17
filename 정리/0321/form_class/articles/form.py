from django import forms
from .models import Article
# form 종류는 2가지
'''
1. Form
사용자의 입력을 받아 개발자가 직접 구성
-> Model 의 필드와 관계없이 마음대로 구성할 수 있다.
- 장점 : 내 마음대로 원하는 입력을 받을 수 있음.
- 단점 : DB에 정확히 저장하기 위해서는 models를 완벽하게 파악
'''
# class ArticleForm(forms.Form):
  # title = forms.CharField(max_length=30)
  # widget: form이 지원하는 기본 필드 외의 추가적인 동작을 원할 때 사용
  # content = forms.CharField(widget=forms.Textarea)


# 2. Model Form
# - Model 에 정의된 필드만 입력받을 수 있음.
# - 장점 : 사용법이 너무 쉽다
# - 단점 : 내 마음대로 입력을 못받는다.
class ArticleForm(forms.ModelForm):
    class Meta:
    # 특정 모델을 참조해야한다.
      model = Article
    # 모든 필드를 입력값을 받겠다.
      fields = "__all__" 
    # 원하는 필드만 입력을 받으려면
    # 주의사항은 튜플, 리스트 형태로 작성해야함 !!!
    # 만약 한개라면 !! , 찍어줘야 튜플임
    # fields = ('title') #<<< 이렇게하면 문자열이고
    # fields = ('title',) #<<< 콤마찍어줘야 튜플임
    #   fields = ('title', 'content', 'author',)

    # 특정 필드를 제외하고 입력을 받고싶으면
    # exclude = ('author',)
      widjets = {
         
      }

