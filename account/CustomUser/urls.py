from django.urls import path
from .views import SignUpView,login_user,LoginView

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)

urlpatterns = [
    path('signup/', SignUpView.as_view(),name='signup'),
    path('login/', login_user, name='login-user'),
    #token
    path('login2/', LoginView.as_view(), name='login'),
    #jwt token
    path('create/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('verify/token/', TokenVerifyView.as_view(), name='verify_token'),
]