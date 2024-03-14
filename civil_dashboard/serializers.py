from rest_framework import serializers
from .models import *

# Serializers for Website Logo Section
class Civil_WebsiteLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_WebsiteLogo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Banner Section
class Civil_WebsiteBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_WebsiteBanner
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website 2 Card Section
class Civil_CardHomepageTwoOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_CardHomepageTwoOne
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class Civil_CardHomepageTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_CardHomepageTwo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Three Card Section
class Civil_CardHomepageThreeOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_CardHomepageThreeOne
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class Civil_CardHomepageThreeTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_CardHomepageThreeTwo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class Civil_CardHomepageThreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_CardHomepageThree
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Four Card Section
class Civil_CardHomepageFourOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_CardHomepageFourOne
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class Civil_CardHomepageFourTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_CardHomepageFourTwo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class Civil_CardHomepageFourThreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_CardHomepageFourThree
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class Civil_CardHomepageFourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_CardHomepageFour
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Template Card Section
class Civil_CardTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_CardTemplate
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Blog Card Section
class Civil_BlogCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_BlogCard
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Timedata Section
class Civil_TimeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_TimeData
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Segment Section
class Civil_Homepage_SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Homepage_Segment
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Website Company Logo Section
class Civil_Support_Company_LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Support_Company_Logo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Global Location Section
class Civil_Global_LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Global_Location
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Contact Section
class Civil_Contact_UsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Contact_Us
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Technology Section
class Civil_TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Technology
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class Civil_Technology_IconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Technology_Icon
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Our Services Section
class Civil_Our_ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Our_Services
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Notice Board Section
class Civil_Notice_BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Notice_Board
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Order Card Section
class Civil_Order_CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Order_Card
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


# Serializers for Security Page Section
class Civil_Security_PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Security_Page
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Company Member Section
class Civil_Company_MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Company_Member
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')





# Serializers for Office Address Section
class Civil_Office_Address_1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Office_Address_1
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class Civil_Office_Address_2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Office_Address_2
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Payment Logo Section
class Civil_Payment_LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Payment_Logo
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Social Media Section
class Civil_Social_MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Social_Media
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')


# Serializers for Subscription Section
class Civil_SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Subscriptions
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Footer Section 1
class Civil_Footer_Section_1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Footer_Section_1
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class Civil_Footer_Section_1_TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Footer_Section_1_Topics
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Footer Section 2
class Civil_Footer_Section_2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Footer_Section_2
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class Civil_Footer_Section_2_TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Footer_Section_2_Topics
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

# Serializers for Footer Section 3
class Civil_Footer_Section_3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Footer_Section_3
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

class Civil_Footer_Section_3_TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civil_Footer_Section_3_Topics
        fields = '__all__'
        read_only_fields = ('created_at', 'last_update_at')

