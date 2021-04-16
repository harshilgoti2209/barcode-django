from .models import Account,Dataitem
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class UserSignUpForm(UserCreationForm):
    email=forms.CharField(widget=forms.EmailInput(attrs={ 'placeholder':'Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder':'password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder':' confirm password'}))
    # password2=forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder':'confirm password'}))
    class Meta:
        model=Account
        fields=('email','password1','password2')

class AuthForm(AuthenticationForm):
    username=forms.CharField(widget=forms.EmailInput(attrs={ 'placeholder':'Email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder':'password'}))
    class Meta:
        model=Account
        fields=('username','password')

class ProfileForm(forms.ModelForm):
    Diabetes=forms.CharField(required=False, label='Diabetes',widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    Cholesterol =forms.CharField(required=False,label='Cholesterol',widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    High_BP =forms.CharField(required=False,label='High BP',widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    Low_BP =forms.CharField(required=False,label='Low BP',widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    Pcos_Pcod =forms.CharField(required=False,label='PCOS/PCOD',widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    Fever =forms.CharField(required=False,label='Fever',widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    Cold =forms.CharField(required=False,label='Cold',widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    Cough =forms.CharField(required=False,label='Cough',widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    Non =forms.CharField(required=False,label='None',widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    class Meta:
        model=Account 
        fields=('Diabetes','Cholesterol','High_BP','Low_BP','Pcos_Pcod','Fever','Cold','Cough','Non')

class AdditemForm(forms.ModelForm):
    calories=forms.IntegerField(required=False,initial=0, label='Calories', widget=forms.NumberInput(attrs={'class':'form-control'}))
    totalfat=forms.CharField(required=False,initial=0, label='Total Fat',widget=forms.NumberInput (attrs={'class':'form-control'}))
    Saturatedfat=forms.CharField(required=False,initial=0, label='Saturated Fat',widget=forms.NumberInput (attrs={'class':'form-control'}))
    Sodium=forms.CharField(required=False,initial=0, label='Sodium',widget=forms.NumberInput(attrs={'class':'form-control'}))
    TotalCarbohydrate=forms.CharField(required=False,initial=0, label='Total Carbohydrate',widget=forms.NumberInput (attrs={'class':'form-control'}))
    DietaryFiber=forms.CharField(required=False,initial=0, label='Dietary Fiber',widget=forms.NumberInput (attrs={'class':'form-control'}))
    Sugar=forms.CharField(required=False,initial=0, label='Sugar',widget=forms.NumberInput (attrs={'class':'form-control'}))
    Protein=forms.CharField(required=False,initial=0, label='Protein',widget=forms.NumberInput (attrs={'class':'form-control'}))
    VitaminD=forms.CharField(required=False,initial=0, label='VitaminD',widget=forms.NumberInput (attrs={'class':'form-control'}))
    Calcium=forms.CharField(required=False,initial=0, label='Calcium',widget=forms.NumberInput (attrs={'class':'form-control'}))
    Iron=forms.CharField(required=False,initial=0, label='Iron',widget=forms.NumberInput (attrs={'class':'form-control'}))
    Potassium=forms.CharField(required=False,initial=0, label='Potassium',widget=forms.NumberInput (attrs={'class':'form-control'}))   

    class Meta:
        model=Dataitem
        fields=('calories','totalfat','Saturatedfat','Sodium','TotalCarbohydrate','DietaryFiber','Sugar','Protein','VitaminD','Calcium','Iron','Potassium')
