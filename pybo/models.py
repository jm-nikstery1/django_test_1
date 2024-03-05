from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)   # 질문의 제목
    content = models.TextField()   #질문의 내용
    create_date = models.DateTimeField()   # 질문 날짜
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')  # 작성자
    modify_date = models.DateTimeField(null=True, blank=True)   # 수정 일시
    voter = models.ManyToManyField(User, related_name='voter_question')   #추천인 추가 - 다대다(N:N) 관계

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='author_answer')  # question이 삭제되면 연결된 answer가 삭제
    content = models.TextField()    # 답변 내용
    create_date = models.DateTimeField()   # 답변 날짜
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #작성자
    modify_date = models.DateTimeField(null=True, blank=True)   #수정 일시
    voter = models.ManyToManyField(User, related_name='voter_answer')  #추천인 추가 - 다대다(N:N) 관계