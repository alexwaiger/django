# -*- coding: utf-8 -*-
from django.contrib import admin

from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

from .models import Payment, Software, Casino, Badge

class CasinoAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'position', 'top_position', 'real_position')
    filter_horizontal = ('country', 'pay')
    search_fields = ('name',)
    ordering = ('-is_active', 'position')
    list_filter = (
        ('is_active'),
        ('country', RelatedDropdownFilter),
        ('license', ChoiceDropdownFilter),
        ('partner', RelatedDropdownFilter),
    )
    list_editable = ('is_active', 'position')
    save_on_top = True
    readonly_fields = ('real_position',)
    fieldsets = (
        ("Important options", {
            'fields': ('is_active', 'name', 'logo', 'link', ('license', 'top_position', 'position'), ('min_dep', 'bonus', 'cashback', 'fs'))
        }),
        ('Advanced options', {
            'fields': ('country', 'pay', ('partner', 'badge'), 'adv1', 'adv2', 'adv3')
        }),
    )

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class BadgeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Casino, CasinoAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Badge, BadgeAdmin)