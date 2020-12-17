from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Resource, FAQ, Form, Info, HealthPlan


class ResourceResource(resources.ModelResource):
    class Meta:
        model = Resource


class FAQResource(resources.ModelResource):
    class Meta:
        model = FAQ


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


class FAQAdmin(ImportExportModelAdmin):
    resource_class = FAQResource


class FormAdmin(ImportExportModelAdmin):
    resource_class = FormResource


class InfoAdmin(ImportExportModelAdmin):
    resource_class = InfoResource


class HealthPlanAdmin(ImportExportModelAdmin):
    resource_class = HealthPlan


admin.site.register(Resource, ResourceAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(Info, InfoAdmin)
admin.site.register(HealthPlan, HealthPlanAdmin)
