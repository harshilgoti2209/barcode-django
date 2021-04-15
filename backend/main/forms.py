from .models import Account,Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserSignUpForm(UserCreationForm):
    email=forms.EmailField(max_length=70)
    class Meta:
        model=Account
        fields=('email','password1','password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('Cholesterol','Bp_high','Bp_low','Pcos_Pcod','Diabetes','Cold')
