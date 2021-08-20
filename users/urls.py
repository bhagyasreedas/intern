from django.urls import path
from users.views import UserRegistrationAPIView, UserLoginAPIView, UserTokenAPIView, GroupList,secret_page

from . import views
app_name = 'users'

urlpatterns = [
    
    path('users/', UserRegistrationAPIView.as_view(), name="list"),
    path('users/login/', UserLoginAPIView.as_view(), name="login"),
    path('tokens/<key>/', UserTokenAPIView.as_view(), name="token"),
    path('groups/', GroupList.as_view()),
    
    path('secret/', views.secret_page, name='secret')
]