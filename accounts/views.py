from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login as user_login
from django.contrib.auth.forms import UserCreationForm
# Django 프레임워크가 구현해 놓은 회원가입 폼을 import 한다.

def signup(request): # urls.py에 views.signup이 이 함수를 가리킨다.
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): # 회원가입 폼에서 적어 보낸 요청이 유효한지 검사한다.
            user = form.save() # 유효한 내용이면 이 회원 정보를 데이터베이스에 저장한다. 그 유저 정보를 리턴한다.
            user_login(request, user) # 유저 정보를 이용해 로그인한다.
        return redirect('accounts:signup')
    	# redirect 시 urls.py의 <app_name>:<name>으로 요청을 보낸다.
    else:
        form = UserCreationForm() # 비어있는 회원가입 폼을 생성한다.
        return render(request, 'accounts/form.html', {'form': form})
    	# forms.html 파일을 렌더한다. 이때 위에서 생성한 회원가입 폼을 'form'이라는 이름으로 함께 보낸다.(딕셔너리)


from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class SignupView(CreateView):
    template_name = 'account/signup.html.j2'
    form_class = UserCreationForm
    success_url = reverse_lazy('signup_done')


class SignupDoneView(TemplateView):
    template_name = 'account/signup_done.html.j2'