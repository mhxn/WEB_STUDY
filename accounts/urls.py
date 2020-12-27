from django.urls import path
from . import views

app_name = "accounts"
# view나 template에서 해당 이름을 이용해 url에 요청을 보낼 수 있다.

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    # "<내 URL>/accounts/signup/" 주소로 요청이 오면 views.py 안에 signup이라는 함수를 찾아 실행한다.
]

from django.urls import path, include
from . import views as account_views

urlpatterns = [
    path('account/signup/', account_views.SignupView.as_view(), name='signup'),
    path('account/signup/done/', account_views.SignupDoneView.as_view(), name='signup_done'),
]