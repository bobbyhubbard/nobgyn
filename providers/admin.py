from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Provider, CertOrg, CertOrgRelationship, School, SchoolRelationship, YoutubeVid


class CertOrgResource(resources.ModelResource):
    class Meta:
        model = CertOrg


class CertOrgAdmin(ImportExportModelAdmin):
    resource_class = CertOrgResource


class ProviderResource(resources.ModelResource):
    class Meta:
        model = Provider


class ProviderAdmin(ImportExportModelAdmin):
    resource_class = ProviderResource
    list_display = ('name', 'view_order')


class YoutubeVidResource(resources.ModelResource):
    class Meta:
        model = YoutubeVid


class YoutubeVidAdmin(ImportExportModelAdmin):
    resource_class = YoutubeVidResource


class CertOrgRelationshipResource(resources.ModelResource):
    class Meta:
        model = CertOrgRelationship


class CertOrgRelationshipAdmin(ImportExportModelAdmin):
    resource_class = CertOrgRelationshipResource


class SchoolResource(resources.ModelResource):
    class Meta:
        model = School


class SchoolAdmin(ImportExportModelAdmin):
    resource_class = SchoolResource


class SchoolRelationshipResource(resources.ModelResource):
    class Meta:
        model = SchoolRelationship


class SchoolRelationshipAdmin(ImportExportModelAdmin):
    resource_class = SchoolRelationshipResource


# Register your models here.
admin.site.register(Provider, ProviderAdmin)
admin.site.register(YoutubeVid, YoutubeVidAdmin)
admin.site.register(CertOrg, CertOrgAdmin)
admin.site.register(CertOrgRelationship, CertOrgRelationshipAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(SchoolRelationship, SchoolRelationshipAdmin)
