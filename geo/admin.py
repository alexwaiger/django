from django.contrib import admin

from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

from .models import Currency, Countries

class CountriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'slug', 'header', 'page_views', 'click')
    list_editable = ('is_active', 'header')
    list_filter = (      
        ('is_active'),
        ('countries', RelatedDropdownFilter),
    )
    fieldsets = (
        ("Important options", {
            'fields': ('is_active', ('name', 'slug'), 'image', 'currency', 'theme', 'rotate', ('pay1', 'pay2'))
        }),
        ('Localisation options', {
            'fields': ('header', 'promo1', 'promo2', 'text', 'tr_license', 'tr_md', 'tr_info', 'tr_bonus', 'tr_fs', 'tr_cashback', 'tr_pay', 'tr_score', 'tr_votes', 'tr_copy', 'tr_play')
        }),
    )
    ordering = ('-is_active', 'slug')
    readonly_fields = ('click', 'page_views')
    
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Countries, CountriesAdmin)
admin.site.register(Currency, CurrencyAdmin)