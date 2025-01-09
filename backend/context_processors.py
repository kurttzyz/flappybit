from . models import User
from payments.models import Deposit, Withdrawal

def Balance(request):
    try:
        user = User.objects.get(email=request.user.email)
        balance =  user.balance
        return {'balance': balance}
    except:
        return {'balance': None}
    


def TotalDeposit(request):
    try:
        user = Deposit.objects.filter(user=request.user)
        amount = 0
        for i in user:
            amount += i.amount
        return {'amount': amount}
    except:
        return {'amount': None}
    


def TotalWithdrawal(request):
    try:
        user = Withdrawal.objects.filter(user=request.user)
        amount = 0
        for i in user:
            amount += i.amount
        return {'bal': amount}
    except:
        return {'bal': None}