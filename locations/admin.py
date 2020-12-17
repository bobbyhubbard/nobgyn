from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Location


class LocationResource(resources.ModelResource):
    class Meta:
        model = Location


class LocationAdmin(ImportExportModelAdmin):
    resource_class = LocationResource


# Register your models here.
admin.site.register(Location, LocationAdmin)
