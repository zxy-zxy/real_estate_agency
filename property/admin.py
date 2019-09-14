from django.contrib import admin

from .models import Flat, Report, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['owner__owner_initials', 'town', 'address']
    readonly_fields = ['created_at']
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        'get_owners',
    ]
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ['likes']


class ReportAdmin(admin.ModelAdmin):
    list_display = ['flat', 'user', 'short_text']
    raw_id_fields = ['flat']


class OwnerAdmin(admin.ModelAdmin):
    list_display = ['owner_initials', 'owner_phonenumber', 'owner_phone_pure']
    raw_id_fields = ['owner_flats']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Owner, OwnerAdmin)
