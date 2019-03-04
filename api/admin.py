from django.contrib import admin
from .models import Offer

# to show dates fields in admin panel


class DateAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date', 'modification_date')


admin.site.register(Offer, DateAdmin)

