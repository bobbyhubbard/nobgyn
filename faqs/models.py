from django.db import models
from django.urls import reverse
from django.utils import http


class FAQ(models.Model):
    # Fields
    slug = models.CharField(
        max_length=50, help_text='URL Path Slug', default='')
    view_order = models.IntegerField(
        default=1, help_text='The display order of this FAQ')
    question = models.TextField(help_text='Frequently asked Question')
    answer = models.TextField(help_text='FAQ Response (html)')
    special = models.TextField(
        help_text='FAQ Response special area (html)', blank=True, null=True)
    old_path = models.CharField(
        max_length=50, help_text='If moved from old site, this is the old faq id (eg "ob_q5")', blank=True, default='')

    @ property
    def type(self):
        return dict(self.faq_types).get(self.faq_type)

    @ property
    def url(self):
        return "faqs:" + dict(self.faq_types).get(self.faq_type)

    def faqTypeName(type):
        return dict(FAQ.faq_types).get(int(type))

    faq_types = (
        (1, "Obstetrics"),
        (2, "Gynecology"),
        (3, "Postoperative"),
    )
    faq_type = models.IntegerField(choices=faq_types, default=1)

    class Meta:
        ordering = ['faq_type', 'view_order']

    # Methods
    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return "/faqs/" + self.slug
