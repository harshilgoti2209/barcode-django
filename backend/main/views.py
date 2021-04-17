from django.shortcuts import render, redirect
from .forms import UserSignUpForm,AuthForm,ProfileForm,AdditemForm
from django.contrib.auth import logout as logout_,login as login_,authenticate,update_session_auth_hash 
from django.views.decorators.csrf import csrf_exempt 
from .models import Account,Dataitem
from django.http import HttpResponse
from django.contrib import messages

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
    return redirect('home')

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

def scan(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method=='POST':
            data=Dataitem.objects.filter(item=request.POST['barcode'])
            if data.count()>0:
                data=Dataitem.objects.get(item=request.POST['barcode'])
                human=Account.objects.get(gmail=request.user)
                if human.Diabetes==True && data.Sugar>230
                return redirect('dashboard')
            else:
                return redirect( 'additem', request.POST['barcode'])

        else:
            return render(request, 'scan.html')
