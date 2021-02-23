from django.db import models
from django.urls import reverse
from django.utils import http


class Location(models.Model):
    # Fields
    slug = models.CharField(
        max_length=25, help_text='URL Path Slug', default='')
    view_order = models.IntegerField(
        default=1, help_text='The display order of this location')
    name = models.CharField(
        max_length=40, help_text='Name', default='')
    parent_facility = models.CharField(
        max_length=40, help_text='The name of the parent facility (eg "Liberty Hospital")', default='', blank=True)
    address1 = models.TextField(
        help_text='Address1', default='')
    address2 = models.TextField(
        help_text='Address2', default='', blank=True)
    city_state_zip = models.TextField(
        help_text='City, State Zip', default='')
    image_sml = models.FileField(
        help_text='Small location image', upload_to='static/images/locations', default='')
    image = models.FileField(
        help_text='Large location image', upload_to='static/images/locations', default='')
    appointment_text = models.TextField(
        help_text='Display text for appointments', default='8am- 5pm  Monday - Friday')
    phone = models.CharField(
        max_length=14, help_text='Phone display text', default='(816) 781-7820')
    fax = models.CharField(
        max_length=14, help_text='Fax display text', default='', blank=True)
    desc = models.TextField(help_text='Description (can be html)', default='')
    highlighted_content = models.TextField(
        help_text='Special content to highlight (can be html)', blank=True, default='')
    isPrimary = models.BooleanField(default=False)

    class Meta:
        ordering = ['view_order']

    # Methods
    def __str__(self):
        _name = self.name
        if self.parent_facility:
            _name += " @ " + self.parent_facility
        return _name

    def get_absolute_url(self):
        return "/locations"
