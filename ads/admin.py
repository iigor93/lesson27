from django.contrib import admin
from .models import Ads, Categories, Location, UserClass


admin.site.register(Ads)
admin.site.register(Categories)
admin.site.register(Location)
admin.site.register(UserClass)
