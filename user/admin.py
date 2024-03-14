from django.contrib import admin
from .models import *

admin.site.register(Website_User)
admin.site.register(UserProfile)
admin.site.register(SocialLink)

admin.site.register(CompanyInformation)
admin.site.register(ContactInformation)
admin.site.register(Address)
