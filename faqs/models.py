from django.db import models
from django.urls import reverse
from django.utils import http


class FAQ(models.Model):
    # Fields
    slug = models.CharField(
        max_length=25, help_text='URL Path Slug', default='')
    view_order = models.IntegerField(
        default=1, help_text='The display order of this FAQ')
    question = models.TextField(help_text='Frequently asked Question')
    answer = models.TextField(help_text='FAQ Response (html)')
    special = models.TextField(
        help_text='FAQ Response special area (html)')
    # Fields
    faq_types = (
        (1, "Obstetric"),
        (2, "Gynecology"),
        (3, "Postoperative"),
    )
    faq_type = models.IntegerField(choices=faq_types, default=1)

    class Meta:
        ordering = ['view_order']

    # Methods
    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return "/faqs/" + self.slug
