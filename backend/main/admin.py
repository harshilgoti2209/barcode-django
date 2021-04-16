from django.contrib import admin
from .models import Account,Dataitem
# Register your models here.

class AdminA(admin.ModelAdmin):
    list_display=('email','Diabetes','Cholesterol','High_BP','Low_BP','Pcos_Pcod','Fever','Cold','Cough','Non')

admin.site.register(Account,AdminA)   

class AdminB(admin.ModelAdmin):
    list_display=('item','calories','totalfat','Saturatedfat','Sodium','TotalCarbohydrate','DietaryFiber','Sugar','Protein','VitaminD','Calcium','Iron','Potassium')

admin.site.register(Dataitem,AdminB)