from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .models import Account

def index(request):
    return render(request, 'accounts/index.html')

def signup_page(request):
    return render(request, 'accounts/signup.html')

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        account = Account.objects.create(
            name=name,
            email=email,
            password=password
        )
        account.save()
        return render(request, 'accounts/login.html')
    return render(request, 'accounts/signup.html')

def login_page(request):
    return render(request, 'accounts/login.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            account = Account.objects.get(email=email)
            if account.password == password:
                return redirect('boards:board_list')
            else:
                return render(request, 'accounts/login.html', {'error': 'Wrong password'})
        except Account.DoesNotExist:
            return render(request, 'accounts/login.html', {'error': 'Account does not exist'})
    
    return render(request, 'accounts/login.html')

@login_required
def logout(request):
    auth_logout(request)
    return render(request, 'accounts/login.html')
