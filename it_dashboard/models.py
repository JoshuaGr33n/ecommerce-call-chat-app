from django.db import models
from django.conf import settings


# =================Website Logo Section Start=======================
# def upload_to_logo(instance, filename):
#     return 'image/it/logo/{filename}'.format(filename=filename)

class IT_WebsiteLogo(models.Model):
    image = models.ImageField(upload_to='it/image/logo/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.image.name}"
# =================Website Logo Section End=======================


# =================Website Banner Section Start=======================
class IT_WebsiteBanner(models.Model):
    header = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    image_and_video = models.FileField(upload_to='it/image/banners/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.header} - {self.tag}"
# =================Website Banner Section End=======================



# =================Website 2 Card Section Start=======================
class IT_CardHomepageTwoOne(models.Model):
    icon = models.ImageField(upload_to='it/image/two-card-icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class IT_CardHomepageTwo(models.Model):
    icon = models.ImageField(upload_to='it/image/two-card-icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
# =================Website 2 Card Section End=======================


# =================Website Three Card Section Start=======================
class IT_CardHomepageThreeOne(models.Model):
    icon = models.ImageField(upload_to='it/image/three-card-icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class IT_CardHomepageThreeTwo(models.Model):
    icon = models.ImageField(upload_to='it/image/three-card-icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class IT_CardHomepageThree(models.Model):
    icon = models.ImageField(upload_to='it/image/three-card-icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
# =================Website Three Card Section End=======================


# =================Website Four Card Section Start=======================
class IT_CardHomepageFourOne(models.Model):
    icon = models.ImageField(upload_to='it/image/four-card-icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class IT_CardHomepageFourTwo(models.Model):
    icon = models.ImageField(upload_to='it/image/four-card-icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class IT_CardHomepageFourThree(models.Model):
    icon = models.ImageField(upload_to='it/image/four-card-icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class IT_CardHomepageFour(models.Model):
    icon = models.ImageField(upload_to='it/image/four-card-icons/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
# =================Website Four Card Section End=======================


# =================Website Template Card Section Start=======================
class IT_CardTemplate(models.Model):
    image = models.ImageField(upload_to='it/image/template-card/', blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=5)
    url = models.URLField()
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
# =================Website Template Card Section End=======================


# =================Website Blog Card Section Start=======================
class IT_BlogCard(models.Model):
    image = models.ImageField(upload_to='it/image/blog-card/',blank=True, null=True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.TextField()
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
# =================Website Blog Card Section End=======================

# =================Website Timedata Section Start=======================
class IT_TimeData(models.Model):
    year = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField()
    day = models.PositiveSmallIntegerField()
    hour = models.PositiveSmallIntegerField()
    second = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.second}"
# =================Website Timedata Section End=======================

# =================Website Segment Section Start=======================
class IT_Homepage_Segment(models.Model):
    photo_or_video = models.FileField(upload_to='it/image/segment/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.photo_or_video.name
# =================Website Segment Section End=======================


# =================Website Company Logo Section Start=======================
class IT_Support_Company_Logo(models.Model):
    logo = models.ImageField(upload_to='it/image/comapny-logo/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.logo.name
# =================Website Company Logo Section End=======================


# =================Website Global Location Section Start=======================
class IT_Global_Location(models.Model):
    flag_logo = models.ImageField(upload_to='it/image/global-location-flag/', blank=True, null=True)
    country_name = models.CharField(max_length=30)
    office_address = models.CharField(max_length=400)
    contact_details = models.CharField(max_length=400)
    
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.country_name
# =================Website Global Location Section End=======================

# =================Website Contact Section Start=======================
class IT_Contact_Us(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=15)
    subject = models.CharField(max_length=600)
    message = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.name} - {self.email}'
# =================Website Contact Section End=======================


# ===========================Technology Start=================================
class IT_Technology(models.Model):
    name = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name

class IT_Technology_Icon(models.Model):
    technology = models.ForeignKey(IT_Technology, on_delete=models.CASCADE, blank=True, null=True)
    icon = models.ImageField(upload_to='it/image/technology-icons/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.technology.name} - {self.icon.name}'
# ===========================Technology End=================================


# ===========================Our Services Start=================================
class IT_Our_Services(models.Model):
    icon = models.ImageField(upload_to='it/image/services-icons/', blank=True, null=True)
    title = models.CharField(max_length=500)
    tags = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
# ===========================Our Services End=================================


# ===========================Notice Board Start=================================
class IT_Notice_Board(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Active', 'Active'),
        ('Deactivate', 'Deactivate'),
        ('Expired', 'Expired'),
    )
    title = models.CharField(max_length=500)
    date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS, default='Active')
    file = models.FileField(upload_to='it/file/notice-board/', blank=True, null=True)
    
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.date} - {self.title}'
# ===========================Notice Board End=================================


# ===========================Order Card Start=================================
class IT_Order_Card(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='it/image/order-card/', blank=True, null=True)
    file = models.FileField(upload_to='it/file/order-card/', blank=True, null=True)
    
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
# ===========================Order Card End=================================


# ===========================Security Page Model Start=================================
class IT_Security_Page(models.Model):
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.description
# ===========================Security Page Model End=================================


# ===========================Company Member Start=================================
class IT_Company_Member(models.Model):
    image = models.ImageField(upload_to='it/image/company-member/', blank=True, null=True)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=14)
    address = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
# ===========================Company Member End=================================






# =================Tow Office Address Section Models Start================
class IT_Office_Address_1(models.Model):
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=140)
    phone = models.CharField(max_length=14)
    fax = models.CharField(max_length=20)
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.address}'

class IT_Office_Address_2(models.Model):
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=140)
    phone = models.CharField(max_length=14)
    fax = models.CharField(max_length=20)
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.address}'
# =================Tow Office Address Section Models End================

# =================Website Payment Logo Section Start=======================
class IT_Payment_Logo(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='it/image/payment-logo/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
# =================Website Payment Logo Section End=======================

# =================Website Social Media Section Start=======================
class IT_Social_Media(models.Model):
    name = models.CharField(max_length=150)
    icon = models.ImageField(upload_to='it/image/social-media-icon/', blank=True, null=True)
    url = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
# =================Website Social Media Section End=======================


# =================Website Subscription Section Start=======================
class IT_Subscriptions(models.Model):
    email = models.EmailField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.email
# =================Website Subscription Section End=======================


# ===========================Footer Section 1 Start=================================
class IT_Footer_Section_1(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
class IT_Footer_Section_1_Topics(models.Model):
    footer_section = models.ForeignKey(IT_Footer_Section_1, on_delete=models.CASCADE, related_name='footer_section_1_topics')
    topic_name = models.CharField(max_length=50)
    topic_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.footer_section.title} - {self.topic_name}'
# ===========================Footer Section 1 End=================================


# ===========================Footer Section 2 Start=================================
class IT_Footer_Section_2(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
class IT_Footer_Section_2_Topics(models.Model):
    footer_section = models.ForeignKey(IT_Footer_Section_2, on_delete=models.CASCADE, related_name='footer_section_2_topics')
    topic_name = models.CharField(max_length=50)
    topic_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.footer_section.title} - {self.topic_name}'
# ===========================Footer Section 2 End=================================


# ===========================Footer Section 3 Start=================================
class IT_Footer_Section_3(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
class IT_Footer_Section_3_Topics(models.Model):
    footer_section = models.ForeignKey(IT_Footer_Section_3, on_delete=models.CASCADE, related_name='footer_section_3_topics')
    topic_name = models.CharField(max_length=50)
    topic_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.footer_section.title} - {self.topic_name}'
# ===========================Footer Section 3 End=================================



class IT_ChatMessage(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='it_sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='it_received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    flag = models.CharField(max_length=255, default="Flag")
    admin_flag = models.CharField(max_length=255, default="Flag")
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

class IT_CallRecording(models.Model):
    caller = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='it_call_recordings_made', on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='it_call_recordings_received', on_delete=models.CASCADE)
    recording = models.FileField(upload_to='static/call_recordings/')
    duration = models.DurationField()
    timestamp = models.DateTimeField(auto_now_add=True)
    flag = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Call from {self.caller} to {self.receiver} on {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['-timestamp']    


