from django.shortcuts import render, redirect
from .forms import UserSignUpForm,AuthForm,ProfileForm,AdditemForm
from django.contrib.auth import logout as logout_,login as login_,authenticate,update_session_auth_hash 
from django.views.decorators.csrf import csrf_exempt 
from .models import Account,Dataitem
from .qrcode import scanner
from django.http import HttpResponse
import pyzbar.pyzbar as pyzbar
import json

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method=="POST":
        fm2=UserSignUpForm(request.POST)
        if fm2.is_valid():
            fm2.save()
            return redirect('login')
        fm=AuthForm()
    else:
        fm2=UserSignUpForm()
        fm=AuthForm()
    return render(request,'login.html',{'form':fm,'form2':fm2,'u':1})  
    
def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard') 
    else:
        if request.method=='POST':
            fm=AuthForm(request=request,data=request.POST)
            if fm.is_valid():
                email=fm.cleaned_data['username']
                password=fm.cleaned_data['password']
                user=authenticate(email=email,password=password)
                if user is not None:
                    login_(request,user)
                    return redirect('login')
            fm2=UserSignUpForm()
        else:
            fm=AuthForm()
            fm2=UserSignUpForm()
        return render(request,'login.html',{'form':fm,'form2':fm2,'u':0})  

def logout(request):
    logout_(request)
    return redirect('login')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        account=Account.objects.get(email=request.user)
        if request.method=='POST':
            fm=ProfileForm(data=request.POST,instance=account)
            if fm.is_valid():
                fm.save()
        else:
            fm=ProfileForm(instance=account)
        return render(request,'dashboard.html',{'form':fm})

def additem(request,name):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method=='POST':
            fm=AdditemForm(request.POST)
            if fm.is_valid():
                a=fm.cleaned_data['calories']
                b=fm.cleaned_data['totalfat']
                c=fm.cleaned_data['Saturatedfat']
                d=fm.cleaned_data['Sodium']
                e=fm.cleaned_data['TotalCarbohydrate']
                f=fm.cleaned_data['DietaryFiber']
                g=fm.cleaned_data['Sugar']
                h=fm.cleaned_data['Protein']
                i=fm.cleaned_data['VitaminD']
                j=fm.cleaned_data['Calcium']
                k=fm.cleaned_data['Iron']
                l=fm.cleaned_data['Potassium']
                item=Dataitem(item=name,calories=a,totalfat=b,Saturatedfat=c,Sodium=d,TotalCarbohydrate=e,DietaryFiber=f,Sugar=g,Protein=h,VitaminD=i,Calcium=j,Iron=k,Potassium=l)
                item.save()
                return redirect('scan')
        else:
            fm=AdditemForm()
        return render(request,'additem.html',{'form':fm})

@csrf_exempt
def scan(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            data = request.POST.get('data')
            print(data)
        else:
            return render(request, 'scan.html')


@csrf_exempt
def scan2(request):
    for key, val in request.POST.items():
        print(json.loads(key)['data'])

    return render(request, 'scan.html')