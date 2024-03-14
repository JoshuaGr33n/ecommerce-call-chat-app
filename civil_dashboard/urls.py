from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .sound_views import *

router = DefaultRouter()
router.register(r'website-logo', Civil_WebsiteLogoViewSet, basename='civil-website-logo')
router.register(r'website-banner', Civil_WebsiteBannerViewSet, basename='civil-website-banner')
router.register(r'card-homepage-two-one', Civil_CardHomepageTwoOneViewSet, basename='civil-card-homepage-two-one')
router.register(r'card-homepage-two', Civil_CardHomepageTwoViewSet, basename='civil-card-homepage-two')
router.register(r'card-homepage-three-one', Civil_CardHomepageThreeOneViewSet, basename='civil-card-homepage-three-one')
router.register(r'card-homepage-three-two', Civil_CardHomepageThreeTwoViewSet, basename='civil-card-homepage-three-two')
router.register(r'card-homepage-three', Civil_CardHomepageThreeViewSet, basename='civil-card-homepage-three')
router.register(r'card-homepage-four-one', Civil_CardHomepageFourOneViewSet, basename='civil-card-homepage-four-one')
router.register(r'card-homepage-four-two', Civil_CardHomepageFourTwoViewSet, basename='civil-card-homepage-four-two')
router.register(r'card-homepage-four-three', Civil_CardHomepageFourThreeViewSet, basename='civil-card-homepage-four-three')
router.register(r'card-homepage-four', Civil_CardHomepageFourViewSet, basename='civil-card-homepage-four')
router.register(r'card-template', Civil_CardTemplateViewSet, basename='civil-card-template')
router.register(r'blog-card', Civil_BlogCardViewSet, basename='civil-blog-card')
router.register(r'time-data', Civil_TimeDataViewSet, basename='civil-time-data')
router.register(r'homepage-segment', Civil_Homepage_SegmentViewSet, basename='civil-homepage-segment')
router.register(r'support-company-logo', Civil_Support_Company_LogoViewSet, basename='civil-support-company-logo')
router.register(r'global-location', Civil_Global_LocationViewSet, basename='civil-global-location')
router.register(r'contact-us', Civil_Contact_UsViewSet, basename='civil-contact-us')
router.register(r'technology', Civil_TechnologyViewSet, basename='civil-technology')
router.register(r'technology-icon', Civil_Technology_IconViewSet, basename='civil-technology-icon')
router.register(r'our-services', Civil_Our_ServicesViewSet, basename='civil-our-services')
router.register(r'notice-board', Civil_Notice_BoardViewSet, basename='civil-notice-board')
router.register(r'order-card', Civil_Order_CardViewSet, basename='civil-order-card')
router.register(r'security-page', Civil_Security_PageViewSet, basename='civil-security-page')
router.register(r'company-member', Civil_Company_MemberViewSet, basename='civil-company-member')
router.register(r'office-address-1', Civil_Office_Address_1ViewSet, basename='civil-office-address-1')
router.register(r'office-address-2', Civil_Office_Address_2ViewSet, basename='civil-office-address-2')
router.register(r'payment-logo', Civil_Payment_LogoViewSet, basename='civil-payment-logo')
router.register(r'social-media', Civil_Social_MediaViewSet, basename='civil-social-media')
router.register(r'subscriptions', Civil_SubscriptionsViewSet, basename='civil-subscriptions')
router.register(r'footer-section-1', Civil_Footer_Section_1ViewSet, basename='civil-footer-section-1')
router.register(r'footer-section-1-topics', Civil_Footer_Section_1_TopicsViewSet, basename='civil-footer-section-1-topics')
router.register(r'footer-section-2', Civil_Footer_Section_2ViewSet, basename='civil-footer-section-2')
router.register(r'footer-section-2-topics', Civil_Footer_Section_2_TopicsViewSet, basename='civil-footer-section-2-topics')
router.register(r'footer-section-3', Civil_Footer_Section_3ViewSet, basename='civil-footer-section-3')
router.register(r'footer-section-3-topics', Civil_Footer_Section_3_TopicsViewSet, basename='civil-footer-section-3-topics')


# ==================================================
# Sound Urls Router For Whole Website Start
# ==================================================
sound_router = DefaultRouter()
sound_router.register(r'live-chat-admin-sound', CivilLiveChatAdminSoundAPI, basename='civil-live-chat-admin-sound')
sound_router.register(r'user-sound', CivilUserSoundAPI, basename='civil-user-sound')
sound_router.register(r'user-order-sound', CivilUserOrderSoundAPI, basename='civil-user-order-sound')
# ==================================================
# Sound Urls Router For Whole Website End
# ==================================================

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('home/', include(router.urls)),
    path('sound/', include(sound_router.urls)),
    
    
    
    
    path('test_socket', test_socket, name='test_socket'),
]
