from django.db import models

# Create your models here.


class Resource(models.Model):
    # Fields
    slug = models.CharField(
        max_length=25, help_text='URL Path Slug', default='')
    view_order = models.IntegerField(
        default=1, help_text='The display order of this resource')
    name = models.CharField(
        max_length=50, help_text='Resource name', default='')
    icon = models.FileField(
        help_text='Icon image for resource', upload_to='static/images/icons', default='')
    isLink = models.BooleanField(
        help_text='Is this menu item an external link?', default=False)
    isFormLink = models.BooleanField(
        help_text='Is this menu item a form submittal?', default=False)
    external_link = models.URLField(
        help_text='External link (optional)', max_length=200, blank=True, default='')
    content = models.TextField(
        help_text='Page content (only if not a link)', blank=True, default='')
    form_content = models.TextField(
        help_text='The raw form html', blank=True, default='')

    class Meta:
        ordering = ['view_order']

    # Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/resources/" + self.slug


class Form(models.Model):

    view_order = models.IntegerField(
        default=1, help_text='The display order of this form')
    name = models.CharField(
        max_length=50, help_text='Form name', default='')
    file = models.FileField(upload_to='forms/', blank=True, default='')
    file_type = models.CharField(max_length=4, blank=True, default='')
    link = models.URLField(
        help_text='Link (optional)', max_length=200, blank=True, default='')

    class Meta:
        ordering = ['view_order']

    def __str__(self):
        return self.name


class Info(models.Model):

    view_order = models.IntegerField(
        default=1, help_text='The display order of this information link')
    name = models.CharField(
        max_length=50, help_text='Link name', default='')
    file = models.FileField(upload_to='info/', blank=True, default='')
    file_type = models.CharField(max_length=4, blank=True, default='')
    link = models.URLField(
        help_text='Link (optional)', max_length=200, blank=True, default='')

    class Meta:
        ordering = ['view_order']

    def __str__(self):
        return self.name


class FAQLink(models.Model):

    view_order = models.IntegerField(
        default=1, help_text='The display order of this FAQ link')
    name = models.CharField(
        max_length=50, help_text='FAQ Link name', default='')
    file = models.FileField(upload_to='faq/', blank=True, default='')
    file_type = models.CharField(max_length=4, blank=True, default='')
    link = models.URLField(
        help_text='Link (optional)', max_length=200, blank=True, default='')

    class Meta:
        ordering = ['view_order']

    def __str__(self):
        return self.name


class HealthPlan(models.Model):

    name = models.CharField(
        max_length=200, help_text='Health Plan name', default='')
    link = models.URLField(
        help_text='Link (optional)', max_length=200, blank=True, default='')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
