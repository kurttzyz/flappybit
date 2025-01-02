from django.urls import path
from . import views


urlpatterns = [
    # Deposit url
    path("deposit/", views.handle_payment_submission, name="deposit"),
 

    # Withdrawal url
    path("withdraw/", views.handle_withdrawal_submission, name="withdraw"),

]
