from django.urls import path
from .views import *
urlpatterns = [
     path('',home,name='home'), 
     path('signup/',signup,name='signup'), 
     # path('signup/signup/',signup,name='signup'), 
     path('login/',login,name='login'), 
     path('logout/',logout,name='loout'), 
     path('dashboard/',dashboard,name='dashboard'), 
     path('additem/<str:name>',additem,name='additem'), 
     path('scan/',scan,name='scan'),  
]
