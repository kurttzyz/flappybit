from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .utils import PasswordReset

from django.contrib.auth.views import (
    LogoutView,
    PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('getbalance/', views.getbalance, name='balance'),
    path('transaction_history/', views.history, name='history'),
<<<<<<< HEAD
    path('getbalance/', views.getbalance, name='balance'),
=======
    path('my_rewards/', views.rewards, name="rewards"),
    path('claim-reward/', views.claim_reward_api, name='claim_reward_api'),
    path('claim-referral-income/', views.claim_referral_income, name='claim-referral-income'),
    path("terms&condition/", views.terms, name="terms"),
>>>>>>> 0244ff341220a700c22737e2212fae206c843efa



    # authentication urls

    path('login/', views.loginview, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),



    # Forgetting password urls
    path('verification/<uidb64>/<token>/', views.EmailVerification, name='verification'),
    path('password_reset/', PasswordReset.as_view(template_name='auths/reset_password.html'), name='reset_password'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='auths/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='auths/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='auths/password_reset_complete.html'), name='password_reset_complete'),






]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)