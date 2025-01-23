from django.shortcuts import render
from django.http import JsonResponse
from . models import *
from django.contrib.auth.decorators import login_required

login_required(login_url='/login')
def minislot(request):

    return render(request, 'games/minislot.html')

login_required(login_url='/login')
def minislotresult(request):
    result1 = request.POST['result1']
    result2 = request.POST['result2']
    result3 = request.POST['result3']
    amount = request.POST['amount']

    Minislot.objects.create(user=request.user, result1=result1, result2=result2, result3=result3, stake=amount)
    user = User.objects.get(email = request.user.email)
    user.balance -= int(amount)
    user.save()
    return JsonResponse({'message': 'successful'})

def flipcoin(request):

    return render(request, 'games/flipcoin.html')

def flipcoinresult(request):

    return JsonResponse({'message': 'successful'})

def rockpaper(request):

    return render(request, 'games/rockpaper.html')

def rockpaperresult(request):

    return JsonResponse({'message': 'successful'})

def bottlespin(request):

    
    return render(request, 'games/bottlespin.html')

def bottlespinresult(request):

    return JsonResponse({'message': 'successful'})
