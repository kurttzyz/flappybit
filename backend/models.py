from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Permission, PermissionsMixin
from django.utils.crypto import get_random_string
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self,email, first_name, last_name, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not first_name:
            raise ValueError('User must enter first name')
        
        if not last_name:
            raise ValueError('User must enter last name')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email,password):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name=last_name,
            password=password,
        )

        permission = Permission.objects.all()

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.user_permissions.set(permission)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    first_name    = models.CharField(max_length=100, blank=True, null=True)
    last_name    = models.CharField(max_length=100, blank=True, null=True)
    email         = models.EmailField(max_length=100, unique=True)
    referal = models.CharField(max_length=20, unique=True, blank=True, null=True)
    refered_by = models.CharField(max_length=50, blank=True, null=True)
    balance = models.IntegerField(default=0)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)

    
    
    date_joined   = models.DateTimeField(auto_now_add=True) 
    last_login    = models.DateTimeField(auto_now_add=True)   
    is_admin      = models.BooleanField(default=False)
    is_staff      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = MyUserManager()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        self.referal = get_random_string(length=5)
        super().save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
    

