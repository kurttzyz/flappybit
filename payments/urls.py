from django.urls import path
from . import views

app_name = 'payments'


urlpatterns = [
    # Deposit url
    path("deposit/", views.make_deposit, name="deposit"),
    path('approve_deposit/<id>', views.approve_deposit, name='approve_deposit'),
    path('deposit_confirmation/', views.deposit_confirmation, name='deposit_confirmation'),

    # Withdrawal url
    path('withdrawal/', views.make_withdrawal, name='withdrawal'),

    # mail url
    path('send_deposit_mail/', views.deposit_confirmation_request, name='deposit_confirm_mail'),


]
