from django.urls import path
from .views import UserSignUpView, UserDetailView, UserScannerView

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('<slug:slug>/profile', UserDetailView.as_view(), name='user_detail'),
    path('scanner/', UserScannerView.as_view(), name='scanner'),
]