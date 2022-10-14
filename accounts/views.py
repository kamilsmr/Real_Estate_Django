from django.shortcuts import render

def register(request):
    return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
