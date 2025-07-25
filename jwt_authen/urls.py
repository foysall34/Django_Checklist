from django.urls import path
from .views import RegisterView, VerifyOTPView, LoginView, ResetPasswordAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
    path('api/register/', RegisterView.as_view()),
    path('api/verify-otp/', VerifyOTPView.as_view()),
    path('api/login/', LoginView.as_view()),
    path('reset-password/', ResetPasswordAPIView.as_view(), name='reset-password'),


]