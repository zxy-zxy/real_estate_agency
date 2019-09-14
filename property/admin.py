from django.contrib import admin

from .models import Flat, Report


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'town', 'address']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ['likes']


class ReportAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat']
    list_display = ['flat', 'user', 'short_text']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Report, ReportAdmin)
