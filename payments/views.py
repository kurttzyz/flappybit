from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from decimal import Decimal
from .form import PaymentForm
from .models import Withdrawal, User

@login_required
def payment_and_withdraw(request):
    if request.method == "POST":
        if "payment_submit" in request.POST:
            handle_payment_submission(request)
        elif "withdraw_submit" in request.POST:
            handle_withdrawal_submission(request)

        # Redirect to prevent duplicate submission  
        return redirect("")  # Replace "dashboard" with your actual dashboard URL name

    # Render the payment and withdrawal page with the payment form (for GET requests)
    return render(request, "", {"form": PaymentForm()})

def handle_payment_submission(request):
    form = PaymentForm(request.POST)
    if form.is_valid():
        try:
            amount = form.cleaned_data['amount']
            if amount < 50:
                messages.error(request, "Minimum deposit amount is 50.")
            else:
                with transaction.atomic():
                    payment = form.save(commit=False)
                    payment.user = request.user
                    payment.status = 'Pending'
                    payment.save()
                messages.success(request, "Payment request submitted for admin approval!")
        except Exception as e:
            messages.error(request, f"Error processing payment: {str(e)}")
    else:
        messages.error(request, "Failed to submit payment: Invalid data.")

def handle_withdrawal_submission(request):
    try:
        # Get form data
        amount = Decimal(request.POST.get("amount", "0"))
        payment_method = request.POST.get("payment_method")
        phone_number = request.POST.get("phone_number")

        # Validate input
        if amount < 160:
            raise ValueError("Minimum withdrawal amount is 160.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if not payment_method or not phone_number:
            raise ValueError("All fields are required.")

        # Check wallet balance
        user = User.objects.get(pk=request.user.pk)
        if user.balance >= amount:
            with transaction.atomic():
                Withdrawal.objects.create(
                    user=request.user,
                    amount=amount,
                    payment_method=payment_method,
                    phone_number=phone_number,
                    status=Withdrawal.PENDING,
                )
                # Deduct the amount from the wallet
                user.balance -= amount
                user.save()
            messages.success(request, "Withdrawal request submitted for admin approval!")
        else:
            messages.error(request, "Insufficient balance!")
    except ValueError as e:
        messages.error(request, f"Error in withdrawal submission: {str(e)}")
    except User.DoesNotExist:
        messages.error(request, "Wallet not found. Please contact support.")
    except Exception as e:
        messages.error(request, f"Unexpected error: {str(e)}")
