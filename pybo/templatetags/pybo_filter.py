'''
템플릿 필터 작성하기

'''
from django import template

register = template.Library()

#템플릿 필터 함수
@register.filter
def sub(value, arg):
    return value - arg