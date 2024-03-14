from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from account.models import Custom_User
from django.contrib.auth.tokens import default_token_generator

# ==============================Model For Website User==================================
class Website_User(Custom_User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    COUNTRY = (
        ('Bangladesh', 'Bangladesh'),
        ('India', 'India'),
        ('US', 'US'),
    )
    full_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    country = models.CharField(max_length=100, choices=COUNTRY)
    
    is_varified = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.username}'


class User_Authentication_Model(models.Model):
    user = models.OneToOneField(Website_User, on_delete=models.CASCADE, related_name='user_authentication')
    otp = models.CharField(max_length=6)
    token = models.CharField(max_length=400)
    
    def save(self, *args, **kwargs):
        token = default_token_generator.make_token(self.user)
        self.token = token
        super(User_Authentication_Model, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.user} - {self.token}'
    

class UserProfile(models.Model):
    MARITAL_STATUS = (
        ('Maride', 'Maride'),
        ('Unmaride', 'Unmaride'),
    )
    user = models.OneToOneField(Website_User, on_delete=models.CASCADE, related_name='user_profile')
    education_qualification = models.CharField(max_length=30, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    occupation = models.CharField(max_length=30, blank=True, null=True)
    monthly_income = models.CharField(max_length=30, blank=True, null=True)
    marital_status = models.CharField(max_length=30, blank=True, null=True, choices=MARITAL_STATUS)
    
    def __str__(self) -> str:
        return f'{self.user.full_name}'


@receiver(post_save, sender=Website_User)
def create_user_authentication_profile_model(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        User_Authentication_Model.objects.create(user=instance)



class CompanyInformation(models.Model):
    user = models.OneToOneField(Website_User, on_delete=models.CASCADE, related_name='user_company_information')
    
    company_name = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)
    company_phone_number = models.CharField(max_length=20)
    company_details = models.TextField(blank=True, null=True)
    company_website = models.URLField()
    
    def __str__(self) -> str:
        return f'{self.user.full_name} | {self.company_name}'

class ContactInformation(models.Model):
    user = models.OneToOneField(Website_User, on_delete=models.CASCADE, related_name='user_contact_information')
    personal_contact = models.CharField(max_length=20)
    home_contact = models.CharField(max_length=20)
    contact_email = models.EmailField(max_length=150)
    contact_address = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name} | {self.personal_contact}'

class SocialLink(models.Model):
    SOCIAL_MEIDA_NAME = (
        ('Facebook', 'Facebook'),
        ('Linkedin', 'Linkedin'),
        ('Instagram', 'Instagram'),
    )
    user = models.ForeignKey(Website_User, on_delete=models.CASCADE, related_name='user_social_link')
    icon_select = models.CharField(max_length=20, choices=SOCIAL_MEIDA_NAME)
    url = models.URLField()
    
    def __str__(self) -> str:
        return f'{self.user.full_name} | {self.icon_select}'

class Address(models.Model):
    user = models.OneToOneField(Website_User, on_delete=models.CASCADE, related_name='user_address')
    street_address = models.CharField(max_length=255)
    state_province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f'{self.user.full_name} | {self.city}'



