from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Faq
from django.db import models


class FaqResource(resources.ModelResource):
    class Meta:
        model = Faq


class FaqAdmin(ImportExportModelAdmin):
    resource_class = FaqResource


admin.site.register(Faq, FaqAdmin)
