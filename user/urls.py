from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *



router = DefaultRouter()
router.register(r'userprofiles', UserProfileAPI, basename='userprofile')
router.register(r'social-link', SocialLinkAPI)
router.register(r'company-information', CompanyInformationAPI)
router.register(r'contact-information', ContactInformationAPI)
router.register(r'address', AddressAPI)

urlpatterns = [
    path('', include(router.urls)),
    
    # User Change Password Api Url====================================
    path('change-password/', ChangePasswordAPIView.as_view(), name='change-password-api'),
    
 
    # User Forget & Reset Password Api Url====================================
    path('forget-password/', ForgetPasswordAPIView.as_view(), name='api-forget-password'),
    path('reset-password/', ResetPasswordAPIView.as_view(), name='api-reset-password'),
    
    path('login/', LoginAPIView.as_view(), name='custom_token_obtain_pair'),
    path('register/', UserRegistrationAPIView.as_view(), name='user_registration'),
    path('verify-otp/', verify_otp, name='verify-otp'),
    path('regenerate-otp/', regenerate_otp, name='regenerate_otp'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('delete-profile-request/', DeleteProfileRequestAPIView.as_view(), name='delete-profile-request'),
    path('cancel-delete-profile-request/', CancelDeleteProfileRequestAPIView.as_view(), name='cancel-delete-profile-request'),
     path('logout/', LogoutAPIView.as_view(), name='logout'),
    
    

]

