from django.contrib import admin
from .models import Partner, Postback

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('postbacks',)

class PostbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_editable = ('is_active',)

admin.site.register(Partner, PartnerAdmin)
admin.site.register(Postback, PostbackAdmin)