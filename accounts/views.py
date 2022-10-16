from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        # print('SUBMITTED REG')
        # return redirect('register')
        return 
    else:
        return render(request, 'accounts/register.html')
def login(request):
    if request.method == 'POST':
        # print('SUBMITTED REG')
        # return redirect('login')
        return 
    else:
        return render(request, 'accounts/login.html')
 

def logout(request):
    return render('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
