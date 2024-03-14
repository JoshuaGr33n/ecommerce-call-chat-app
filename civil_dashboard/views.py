from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import *
from django.shortcuts import render

# Viewsets for Website Logo Section
class Civil_WebsiteLogoViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    # permission_classes = [IsAuthenticated]
    queryset = Civil_WebsiteLogo.objects.all()
    serializer_class = Civil_WebsiteLogoSerializer

# Viewsets for Website Banner Section
class Civil_WebsiteBannerViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_WebsiteBanner.objects.all()
    serializer_class = Civil_WebsiteBannerSerializer

# Viewsets for Website 2 Card Section
class Civil_CardHomepageTwoOneViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_CardHomepageTwoOne.objects.all()
    serializer_class = Civil_CardHomepageTwoOneSerializer

class Civil_CardHomepageTwoViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_CardHomepageTwo.objects.all()
    serializer_class = Civil_CardHomepageTwoSerializer

# Viewsets for Website Three Card Section
class Civil_CardHomepageThreeOneViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_CardHomepageThreeOne.objects.all()
    serializer_class = Civil_CardHomepageThreeOneSerializer

class Civil_CardHomepageThreeTwoViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_CardHomepageThreeTwo.objects.all()
    serializer_class = Civil_CardHomepageThreeTwoSerializer

class Civil_CardHomepageThreeViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_CardHomepageThree.objects.all()
    serializer_class = Civil_CardHomepageThreeSerializer

# Viewsets for Website Four Card Section
class Civil_CardHomepageFourOneViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_CardHomepageFourOne.objects.all()
    serializer_class = Civil_CardHomepageFourOneSerializer

class Civil_CardHomepageFourTwoViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_CardHomepageFourTwo.objects.all()
    serializer_class = Civil_CardHomepageFourTwoSerializer

class Civil_CardHomepageFourThreeViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_CardHomepageFourThree.objects.all()
    serializer_class = Civil_CardHomepageFourThreeSerializer

class Civil_CardHomepageFourViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_CardHomepageFour.objects.all()
    serializer_class = Civil_CardHomepageFourSerializer

# Viewsets for Website Template Card Section
class Civil_CardTemplateViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_CardTemplate.objects.all()
    serializer_class = Civil_CardTemplateSerializer

# Viewsets for Website Blog Card Section
class Civil_BlogCardViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_BlogCard.objects.all()
    serializer_class = Civil_BlogCardSerializer

# Viewsets for Website Timedata Section
class Civil_TimeDataViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_TimeData.objects.all()
    serializer_class = Civil_TimeDataSerializer

# Viewsets for Website Segment Section
class Civil_Homepage_SegmentViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Homepage_Segment.objects.all()
    serializer_class = Civil_Homepage_SegmentSerializer

# Viewsets for Website Company Logo Section
class Civil_Support_Company_LogoViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Support_Company_Logo.objects.all()
    serializer_class = Civil_Support_Company_LogoSerializer

# Viewsets for Global Location Section
class Civil_Global_LocationViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Global_Location.objects.all()
    serializer_class = Civil_Global_LocationSerializer

# Viewsets for Contact Section
class Civil_Contact_UsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Contact_Us.objects.all()
    serializer_class = Civil_Contact_UsSerializer

# Viewsets for Technology Section
class Civil_TechnologyViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Technology.objects.all()
    serializer_class = Civil_TechnologySerializer

class Civil_Technology_IconViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Technology_Icon.objects.all()
    serializer_class = Civil_Technology_IconSerializer

# Viewsets for Our Services Section
class Civil_Our_ServicesViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Our_Services.objects.all()
    serializer_class = Civil_Our_ServicesSerializer

# Viewsets for Notice Board Section
class Civil_Notice_BoardViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Notice_Board.objects.all()
    serializer_class = Civil_Notice_BoardSerializer

# Viewsets for Order Card Section
class Civil_Order_CardViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Order_Card.objects.all()
    serializer_class = Civil_Order_CardSerializer

# Viewsets for Security Page Section
class Civil_Security_PageViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Security_Page.objects.all()
    serializer_class = Civil_Security_PageSerializer

# Viewsets for Company Member Section
class Civil_Company_MemberViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Company_Member.objects.all()
    serializer_class = Civil_Company_MemberSerializer



# Viewsets for Office Address Section
class Civil_Office_Address_1ViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Office_Address_1.objects.all()
    serializer_class = Civil_Office_Address_1Serializer

class Civil_Office_Address_2ViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Office_Address_2.objects.all()
    serializer_class = Civil_Office_Address_2Serializer

# Viewsets for Payment Logo Section
class Civil_Payment_LogoViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Payment_Logo.objects.all()
    serializer_class = Civil_Payment_LogoSerializer

# Viewsets for Social Media Section
class Civil_Social_MediaViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Social_Media.objects.all()
    serializer_class = Civil_Social_MediaSerializer

# Viewsets for Subscription Section
class Civil_SubscriptionsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Subscriptions.objects.all()
    serializer_class = Civil_SubscriptionsSerializer

# Viewsets for Footer Section 1
class Civil_Footer_Section_1ViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Footer_Section_1.objects.all()
    serializer_class = Civil_Footer_Section_1Serializer

class Civil_Footer_Section_1_TopicsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Footer_Section_1_Topics.objects.all()
    serializer_class = Civil_Footer_Section_1_TopicsSerializer

# Viewsets for Footer Section 2
class Civil_Footer_Section_2ViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Footer_Section_2.objects.all()
    serializer_class = Civil_Footer_Section_2Serializer

class Civil_Footer_Section_2_TopicsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Footer_Section_2_Topics.objects.all()
    serializer_class = Civil_Footer_Section_2_TopicsSerializer

# Viewsets for Footer Section 3
class Civil_Footer_Section_3ViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Footer_Section_3.objects.all()
    serializer_class = Civil_Footer_Section_3Serializer

class Civil_Footer_Section_3_TopicsViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Civil_Footer_Section_3_Topics.objects.all()
    serializer_class = Civil_Footer_Section_3_TopicsSerializer


def test_socket(request):
    
    return render(request, 'test-socket.html',{})