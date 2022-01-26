from django.contrib import admin

from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

from .models import Currency, Countries

class CountriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'slug', 'header')
    list_editable = ('is_active', 'header')
    list_filter = (      
        ('is_active'),
        ('countries', RelatedDropdownFilter),
    )
    ordering = ('-is_active', 'slug')
    
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Countries, CountriesAdmin)
admin.site.register(Currency, CurrencyAdmin)