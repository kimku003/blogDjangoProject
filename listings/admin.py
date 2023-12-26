from django.contrib import admin
from listings.models import Band
from listings.models import Listing
from listings.models import Desert



class BandAdmin(admin.ModelAdmin): 
    list_display = ('name', 'genre')
admin.site.register(Band, BandAdmin)

class ListingAdmin(admin.ModelAdmin): 
    list_display = ('name', 'type')

admin.site.register(Listing, ListingAdmin)

class DesertAdmin(admin.ModelAdmin): 
    list_display = ('name', 'category')

admin.site.register(Desert, DesertAdmin)
