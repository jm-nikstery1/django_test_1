'''
질문 등록을 위한 폼(form)
답변 등록을 위한 폼
'''
from django import forms
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question # 사용할 모델
        fields = ['subject','content']  #QuestionForm에서 사용할 Question 모델의 속성
        label = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용'
        }