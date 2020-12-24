from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Resource, FAQLink, Form, Info, HealthPlan


class ResourceResource(resources.ModelResource):
    class Meta:
        model = Resource


class FAQLinkResource(resources.ModelResource):
    class Meta:
        model = FAQLink


class FormResource(resources.ModelResource):
    class Meta:
        model = Form


class InfoResource(resources.ModelResource):
    class Meta:
        model = Info


class HealthPlanResource(resources.ModelResource):
    class Meta:
        model = HealthPlan


class ResourceAdmin(ImportExportModelAdmin):
    resource_class = ResourceResource


class FAQLinkAdmin(ImportExportModelAdmin):
    resource_class = FAQLinkResource


class FormAdmin(ImportExportModelAdmin):
    resource_class = FormResource


class InfoAdmin(ImportExportModelAdmin):
    resource_class = InfoResource


class HealthPlanAdmin(ImportExportModelAdmin):
    resource_class = HealthPlanResource


admin.site.register(Resource, ResourceAdmin)
admin.site.register(FAQLink, FAQLinkAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(Info, InfoAdmin)
admin.site.register(HealthPlan, HealthPlanAdmin)
