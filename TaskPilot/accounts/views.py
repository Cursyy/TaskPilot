from django.shortcuts import render, redirect
from .models import Account

# Create your views here.

def signup_page(request):
    return render(request, 'accounts/signup.html')

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        print(name)
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
        print(email,password)
        account = Account.objects.get(email=email)
        if account.password == password:
            return redirect('boards:board_list')
        else:
            return render(request, 'accounts/login.html', {'error': 'Wrong password'})
    
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/login.html')

def index(request):
    return render(request, 'accounts/index.html')