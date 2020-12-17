from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Banner


class BannerResource(resources.ModelResource):
    class Meta:
        model = Banner


class BannerAdmin(ImportExportModelAdmin):
    resource_class = BannerResource
    list_display = ('message', 'is_active')


admin.site.register(Banner, BannerAdmin)
