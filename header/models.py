from django.db import models
from django.urls import reverse
from django.utils import http, timezone
from datetime import datetime, date, timedelta


class Banner(models.Model):

    def one_year_from_today():
        return timezone.now() + timedelta(days=365.25)

    message = models.TextField(
        help_text='What should this banner message say?', default='')
    publish_date = models.DateTimeField(
        help_text='When should this banner message be published?', default=datetime.now)
    expiration_date = models.DateTimeField(
        help_text='When should this banner stop being displayed? (Defaults 1 year from now)', default=one_year_from_today)

    def __str__(self):
        return self.message

    @ property
    def is_active(self):
        return (timezone.now() > self.publish_date) & (timezone.now() < self.expiration_date)
