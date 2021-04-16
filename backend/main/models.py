from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError('please enter your email')

        user= self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user= self.create_user(
            email=self.normalize_email(email),
            password=password
        ) 
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email=models.EmailField(max_length=70,unique=True, verbose_name="Email")
    date_joined=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login=models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)    

    
    Diabetes=models.BooleanField(default=False)    
    Cholesterol=models.BooleanField(default=False)    
    High_BP=models.BooleanField(default=False)    
    Low_BP=models.BooleanField(default=False)    
    Pcos_Pcod=models.BooleanField(default=False)    
    Fever=models.BooleanField(default=False)    
    Cold=models.BooleanField(default=False)    
    Cough=models.BooleanField(default=False)    
    Non=models.BooleanField(default=False)    

    
    USERNAME_FIELD='email'

    objects=MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Dataitem(models.Model):
    item=models.CharField(max_length=100 ,primary_key=True)
    calories=models.IntegerField()
    totalfat=models.IntegerField()
    Saturatedfat=models.IntegerField()
    Sodium=models.IntegerField()
    TotalCarbohydrate=models.IntegerField()
    DietaryFiber=models.IntegerField()
    Sugar=models.IntegerField()
    Protein=models.IntegerField()
    VitaminD=models.IntegerField()
    Calcium=models.IntegerField()
    Iron=models.IntegerField()
    Potassium=models.IntegerField()