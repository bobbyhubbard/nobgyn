from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from faqs.models import FAQ
from django.db import models


class FAQResource(resources.ModelResource):
    class Meta:
        model = FAQ


class FAQAdmin(ImportExportModelAdmin):
    resource_class = FAQResource
    list_display = ('question', 'faq_type')


admin.site.register(FAQ, FAQAdmin)
