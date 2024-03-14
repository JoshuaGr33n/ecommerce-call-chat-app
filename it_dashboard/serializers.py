from rest_framework import serializers
from .models import *

# Serializers for Website Logo Section
class IT_WebsiteLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_WebsiteLogo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Banner Section
class IT_WebsiteBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_WebsiteBanner
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website 2 Card Section
class IT_CardHomepageTwoOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_CardHomepageTwoOne
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class IT_CardHomepageTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_CardHomepageTwo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Three Card Section
class IT_CardHomepageThreeOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_CardHomepageThreeOne
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class IT_CardHomepageThreeTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_CardHomepageThreeTwo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class IT_CardHomepageThreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_CardHomepageThree
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Four Card Section
class IT_CardHomepageFourOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_CardHomepageFourOne
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class IT_CardHomepageFourTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_CardHomepageFourTwo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class IT_CardHomepageFourThreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_CardHomepageFourThree
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class IT_CardHomepageFourSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_CardHomepageFour
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Template Card Section
class IT_CardTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_CardTemplate
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Blog Card Section
class IT_BlogCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_BlogCard
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Timedata Section
class IT_TimeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_TimeData
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Segment Section
class IT_Homepage_SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Homepage_Segment
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Company Logo Section
class IT_Support_Company_LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Support_Company_Logo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Global Location Section
class IT_Global_LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Global_Location
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Contact Section
class IT_Contact_UsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Contact_Us
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


# Serializers for Technology Section
class IT_TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Technology
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class IT_Technology_IconSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Technology_Icon
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Our Services Section
class IT_Our_ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Our_Services
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Notice Board Section
class IT_Notice_BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Notice_Board
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Order Card Section
class IT_Order_CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Order_Card
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


# Serializers for Security Page Section
class IT_Security_PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Security_Page
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Company Member Section
class IT_Company_MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Company_Member
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')




# Serializers for Office Address Section
class IT_Office_Address_1Serializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Office_Address_1
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class IT_Office_Address_2Serializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Office_Address_2
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Payment Logo Section
class IT_Payment_LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Payment_Logo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Social Media Section
class IT_Social_MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Social_Media
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Subscription Section
class IT_SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Subscriptions
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Footer Section 1
class IT_Footer_Section_1Serializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Footer_Section_1
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class IT_Footer_Section_1_TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Footer_Section_1_Topics
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Footer Section 2
class IT_Footer_Section_2Serializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Footer_Section_2
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class IT_Footer_Section_2_TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Footer_Section_2_Topics
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Footer Section 3
class IT_Footer_Section_3Serializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Footer_Section_3
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class IT_Footer_Section_3_TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Footer_Section_3_Topics
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')



