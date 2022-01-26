# -*- coding: utf-8 -*-
from django.contrib import admin

from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

from .models import Payment, Software, Casino, Badge

class CasinoAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'position')
    filter_horizontal = ('country', 'pay')
    search_fields = ('name',)
    ordering = ('-is_active', 'position')
    fieldsets = (
        (None, {
            'fields': (('is_active', 'name', 'partner'), ('trust_score', 'votes', 'license', 'badge'), 'logo', 'country', ('min_dep', 'bonus', 'limit', 'fs'))
        }),
        ('Australian Top', {
            'classes': ('collapse',),
            'fields': ('pay', ('position', 'link'), ('adv1', 'adv2', 'adv3'))
        })
    )
    list_filter = (      
        ('is_active'),
        ('country', RelatedDropdownFilter),
        ('license', ChoiceDropdownFilter),
        ('partner', RelatedDropdownFilter),
    )
    list_editable = ('is_active', 'position')
    save_on_top = True

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name',)      

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BadgeAdmin(admin.ModelAdmin):
    list_display = ('name',)      
    
admin.site.register(Casino, CasinoAdmin)
admin.site.register(Payment, SoftwareAdmin)
admin.site.register(Software, PaymentAdmin)
admin.site.register(Badge, BadgeAdmin)