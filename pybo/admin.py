from django.contrib import admin
from .models import Question

# Register your models here.

#모델 검색
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

# 모델 관리
admin.site.register(Question, QuestionAdmin)