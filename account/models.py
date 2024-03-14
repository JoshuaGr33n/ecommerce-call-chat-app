from django.db import models
from .managers import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from django.utils import timezone
import datetime





# ==============================Custom User==================================
class Custom_User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True, validators=[UnicodeUsernameValidator])
    email = models.EmailField(max_length=40, unique=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    
    date_joined = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
    is_verified = models.BooleanField(default=False)
    request_delete = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    deleted_date = models.DateTimeField(null=True, blank=True)
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        ordering = ['-date_joined']
    
    def __str__(self) -> str:
        return self.username


class UserOTP(models.Model):
    user = models.OneToOneField(Custom_User, on_delete=models.CASCADE, related_name='otp')
    otp = models.IntegerField(null=True, blank=True)
    otp_expiry = models.DateTimeField(null=True, blank=True)
    OTP_TYPE = (
        ('Password', 'Password'),
        ('Login', 'Login'),
    )
    otp_type = models.CharField(choices=OTP_TYPE, blank=True, null=True, max_length=50, default='Login')

    def set_otp(self, otp, type):
        self.otp = otp
        self.otp_type = type
        self.otp_expiry = timezone.now() + datetime.timedelta(minutes=5)  # OTP expires in 5 minutes
        self.save()

    def verify_otp(self, otp, type):
        if timezone.now() <= self.otp_expiry and self.otp == otp and self.otp_type == type:
            self.otp = None  # Clear OTP after successful verification
            if type == "Login":
                self.user.is_verified = True  # Update the is_verified attribute
            self.otp_type = None
            self.user.save() 
            self.save()
            return True
        return False






