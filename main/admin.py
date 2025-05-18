from django.contrib import admin
from .models import *

class UstozAdmin(admin.ModelAdmin):
    search_fields = ['ism']

class YonalishAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'aktiv')
    list_display_links = ('id', 'nom')
    list_filter = ['aktiv']
    search_fields = ['nom']

class FanAdmin(admin.ModelAdmin):
    list_display = ('nom', 'asosiy', 'yonalish')
    list_filter = ('asosiy', 'yonalish__nom')
    search_fields = ['nom']

admin.site.register(Fan, FanAdmin,)
admin.site.register(Yonalish, YonalishAdmin,)
admin.site.register(Ustoz, UstozAdmin,)

