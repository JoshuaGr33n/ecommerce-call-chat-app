from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import *

# Viewsets for Website Logo Section
class IT_WebsiteLogoViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_WebsiteLogo.objects.all()
    serializer_class = IT_WebsiteLogoSerializer

# Viewsets for Website Banner Section
class IT_WebsiteBannerViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_WebsiteBanner.objects.all()
    serializer_class = IT_WebsiteBannerSerializer

# Viewsets for Website 2 Card Section
class IT_CardHomepageTwoOneViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_CardHomepageTwoOne.objects.all()
    serializer_class = IT_CardHomepageTwoOneSerializer

class IT_CardHomepageTwoViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_CardHomepageTwo.objects.all()
    serializer_class = IT_CardHomepageTwoSerializer

# Viewsets for Website Three Card Section
class IT_CardHomepageThreeOneViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_CardHomepageThreeOne.objects.all()
    serializer_class = IT_CardHomepageThreeOneSerializer

class IT_CardHomepageThreeTwoViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_CardHomepageThreeTwo.objects.all()
    serializer_class = IT_CardHomepageThreeTwoSerializer

class IT_CardHomepageThreeViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_CardHomepageThree.objects.all()
    serializer_class = IT_CardHomepageThreeSerializer

# Viewsets for Website Four Card Section
class IT_CardHomepageFourOneViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_CardHomepageFourOne.objects.all()
    serializer_class = IT_CardHomepageFourOneSerializer

class IT_CardHomepageFourTwoViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_CardHomepageFourTwo.objects.all()
    serializer_class = IT_CardHomepageFourTwoSerializer

class IT_CardHomepageFourThreeViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_CardHomepageFourThree.objects.all()
    serializer_class = IT_CardHomepageFourThreeSerializer

class IT_CardHomepageFourViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_CardHomepageFour.objects.all()
    serializer_class = IT_CardHomepageFourSerializer

# Viewsets for Website Template Card Section
class IT_CardTemplateViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_CardTemplate.objects.all()
    serializer_class = IT_CardTemplateSerializer

# Viewsets for Website Blog Card Section
class IT_BlogCardViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_BlogCard.objects.all()
    serializer_class = IT_BlogCardSerializer

# Viewsets for Website Timedata Section
class IT_TimeDataViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_TimeData.objects.all()
    serializer_class = IT_TimeDataSerializer

# Viewsets for Website Segment Section
class IT_Homepage_SegmentViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Homepage_Segment.objects.all()
    serializer_class = IT_Homepage_SegmentSerializer

# Viewsets for Website Company Logo Section
class IT_Support_Company_LogoViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Support_Company_Logo.objects.all()
    serializer_class = IT_Support_Company_LogoSerializer

# Viewsets for Global Location Section
class IT_Global_LocationViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Global_Location.objects.all()
    serializer_class = IT_Global_LocationSerializer

# Viewsets for Contact Section
class IT_Contact_UsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Contact_Us.objects.all()
    serializer_class = IT_Contact_UsSerializer

# Viewsets for Technology Section
class IT_TechnologyViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Technology.objects.all()
    serializer_class = IT_TechnologySerializer

class IT_Technology_IconViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Technology_Icon.objects.all()
    serializer_class = IT_Technology_IconSerializer

# Viewsets for Our Services Section
class IT_Our_ServicesViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Our_Services.objects.all()
    serializer_class = IT_Our_ServicesSerializer

# Viewsets for Notice Board Section
class IT_Notice_BoardViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Notice_Board.objects.all()
    serializer_class = IT_Notice_BoardSerializer

# Viewsets for Order Card Section
class IT_Order_CardViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    permission_classes = (AllowAny,)
    queryset = IT_Order_Card.objects.all()
    serializer_class = IT_Order_CardSerializer

# Viewsets for Security Page Section
class IT_Security_PageViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Security_Page.objects.all()
    serializer_class = IT_Security_PageSerializer

# Viewsets for Company Member Section
class IT_Company_MemberViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Company_Member.objects.all()
    serializer_class = IT_Company_MemberSerializer





# Viewsets for Office Address Section
class IT_Office_Address_1ViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Office_Address_1.objects.all()
    serializer_class = IT_Office_Address_1Serializer

class IT_Office_Address_2ViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Office_Address_2.objects.all()
    serializer_class = IT_Office_Address_2Serializer

# Viewsets for Payment Logo Section
class IT_Payment_LogoViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Payment_Logo.objects.all()
    serializer_class = IT_Payment_LogoSerializer

# Viewsets for Social Media Section
class IT_Social_MediaViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Social_Media.objects.all()
    serializer_class = IT_Social_MediaSerializer

# Viewsets for Subscription Section
class IT_SubscriptionsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Subscriptions.objects.all()
    serializer_class = IT_SubscriptionsSerializer

# Viewsets for Footer Section 1
class IT_Footer_Section_1ViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Footer_Section_1.objects.all()
    serializer_class = IT_Footer_Section_1Serializer

class IT_Footer_Section_1_TopicsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Footer_Section_1_Topics.objects.all()
    serializer_class = IT_Footer_Section_1_TopicsSerializer

# Viewsets for Footer Section 2
class IT_Footer_Section_2ViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Footer_Section_2.objects.all()
    serializer_class = IT_Footer_Section_2Serializer

class IT_Footer_Section_2_TopicsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Footer_Section_2_Topics.objects.all()
    serializer_class = IT_Footer_Section_2_TopicsSerializer

# Viewsets for Footer Section 3
class IT_Footer_Section_3ViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Footer_Section_3.objects.all()
    serializer_class = IT_Footer_Section_3Serializer

class IT_Footer_Section_3_TopicsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = IT_Footer_Section_3_Topics.objects.all()
    serializer_class = IT_Footer_Section_3_TopicsSerializer

