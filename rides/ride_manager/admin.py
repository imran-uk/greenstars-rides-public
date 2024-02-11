from django.contrib import admin

# Register your models here.
from .models import *

class RideAdmin(admin.ModelAdmin):
    save_as = True

admin.site.register(Ride, RideAdmin)
admin.site.register(RideType)
admin.site.register(MeetingPoint)
admin.site.register(Rider)