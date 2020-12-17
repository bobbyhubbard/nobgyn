from django.db import models
from django.urls import reverse
from django.utils import http


class Faq(models.Model):
    # Fields
    slug = models.CharField(
        max_length=25, help_text='URL Path Slug', default='')
    view_order = models.IntegerField(
        default=1, help_text='The display order of this FAQ')
    question = models.TextField(
        help_text='Frequently asked Question', blank=False, null=False)
    answer = models.TextField(
        help_text='FAQ Response (html)', blank=False, null=False)

    class Meta:
        ordering = ['view_order']

    # Methods
    def get_absolute_url(self):
        return "/faqs/" + self.slug

    def __str__(self):
        return self.question
