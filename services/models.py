from django.db import models


class Service(models.Model):
    # Fields
    slug = models.CharField(
        max_length=25, help_text='URL Path Slug', default='')
    view_order = models.IntegerField(
        default=1, help_text='The display order of this service')
    name = models.CharField(
        max_length=50, help_text='Service name', default='')
    icon = models.FileField(
        help_text='Icon image for service', upload_to='static/images/icons', default='')
    summary_desc = models.TextField(
        help_text='Description for the main Services page (can be html)', default='')
    desc = models.TextField(help_text='Description (can be html)', default='')
    services = models.TextField(help_text='Services (can be html)')
    sidebar = models.TextField(help_text='Sidebar (can be html)')

    class Meta:
        ordering = ['view_order']

    # Methods
    def get_absolute_url(self):
        return "/services/" + self.slug

    def __str__(self):
        return self.slug
