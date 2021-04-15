from django.shortcuts import render, redirect
from .forms import UserSignUpForm
from django.contrib.auth import logout as logout_,login as login_,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm 
from django.views.decorators.csrf import csrf_exempt 
from .models import Profile
from .qrcode import scanner
# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method=="POST":
        fm=UserSignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=UserSignUpForm()
    return render(request,'signup.html',{'form':fm})
    
def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard') 
    else:
        if request.method=='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                email=fm.cleaned_data['username']
                password=fm.cleaned_data['password']
                user=authenticate(email=email,password=password)
                if user is not None:
                    login_(request,user)
                    return redirect('login')
        else:
            fm=AuthenticationForm()
        return render(request,'login.html',{'form':fm})

def logout(request):
    logout_(request)
    return redirect('login')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        account=Profile.objects.get(Email=request.user)
        return render(request,'dashboard.html',{'profile':account})

def scan(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method=='POST':
            data=request.POST.get('data')
            print(data)
        else:
            return render(request,'scan.html')
@csrf_exempt
def scan2(request):
    for key, value in request.POST.items():
        print ("%s %s" % (key, value))
    print('hello')
    return 'sqasa'
