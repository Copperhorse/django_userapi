from django.urls import path
from .views import RegisterAPI, LoginAPI, ForgotPasswordAPI, UserDataAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordAPI.as_view(), name='forgot-password'),
    path('user-data/', UserDataAPI.as_view(), name='user-data'),
]
