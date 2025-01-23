from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decimal import Decimal
from .form import PaymentForm, WithdrawalForm
from .models import Withdrawal, User, Deposit
from django.http import JsonResponse, HttpResponse
from .utils import DepositConfirmationMail


def make_withdrawal(request):
    if request.method == 'POST':
        form = WithdrawalForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            user = User.objects.get(email= request.user.email)

            if data.amount <= 500:
                messages.error(request, 'The minimum withdrawal amount is 500 pesos.')
                return redirect('/withdrawal')
            
            if data.amount <= user.balance:
                user.balance -= data.amount
                user.save()
                data.save()
                return redirect('/profile')
            else:
                messages.success(request, 'Insufficient Balance')
                return redirect('/withdrawal')
    else:
        form =  WithdrawalForm()
    args = {'form': form}
    return render(request, 'payments/withdrawal.html', args)




def make_deposit(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            depositform= form.save(commit=False)
            depositform.user = request.user
            if not Deposit.objects.filter(reference_number = depositform.reference_number).exists():
                depositform.save()
            else:
                pass
            return render(request, 'payments/confirmpayment.html', {'currency':depositform.payment_method, 'amount':depositform.amount, 'id':depositform.pk})
    else:
        form = PaymentForm()
    args = {'form': form}

    return render(request, 'payments/deposit.html', args)

#  GETS DEPOSIT STATUS
def deposit_confirmation(request):
    payment_status = Deposit.objects.filter(user = request.user).last()
    if payment_status.status == 'Approved':
        return JsonResponse({'status': 'Completed'})
    else:
        return JsonResponse({'status': 'Pending'})
    
# 
def deposit_confirmation_request(request):
    if request.method == 'POST':
        user =  User.objects.get(email =request.user.email)
        deposit_id = request.POST['id']
        try:
            data = Deposit.objects.get(user=request.user, pk = deposit_id)
            DepositConfirmationMail(request, data)
            return JsonResponse({'message': 'Confirmation Request Sent'})
        except:
            DepositConfirmationMail(request, data)
            return JsonResponse({'message': 'Confirmation Request Sending Failed'})
        

def approve_deposit(request, id):
    try:
        deposit = Deposit.objects.get(pk = int(id), user=request.user)
        if deposit.status == 'Pending':
            deposit.status = 'Approved'
            deposit.user.balance += deposit.amount
            deposit.user.save()
            deposit.save()
            return HttpResponse('Approved')
    except:
        return HttpResponse('Deposit not found confirm with the reference number')


