from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),  #view를 따로 만들지 않고 django의 로그인뷰 사용
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),  #회원가입 url
    ]