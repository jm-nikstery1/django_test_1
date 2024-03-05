from django.contrib.auth import authenticate, login, logout  # 로그아웃, 로그인, 인증
from django.shortcuts import redirect, render
from common.forms import UserForm

# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('index')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')

    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
