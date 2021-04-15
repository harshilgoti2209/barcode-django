from django.contrib import admin
from .models import Account,Profile
# Register your models here.

class AdminA(admin.ModelAdmin):
    fields=('email','password')

admin.site.register(Account,AdminA)   

class ProfileA(admin.ModelAdmin):
    fields=('Email','Cholesterol','Bp_high','Bp_low','Pcos_Pcod','Diabetes','Cold')

admin.site.register(Profile,ProfileA)