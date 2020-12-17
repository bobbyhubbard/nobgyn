from django.db import models
from django.urls import reverse
from django.utils import http


class Provider(models.Model):
    # Fields
    view_order = models.IntegerField(
        default=1, help_text='The display order of this provider')
    slug = models.CharField(
        max_length=25, help_text='URL Path Slug', default='')
    name = models.CharField(max_length=50, help_text='Full name with creds')
    focus = models.CharField(
        max_length=50, help_text='Ob, Gyn, or both?', default='Obstetrics & Gynecology')
    doctor = models.BooleanField(default=True)
    bio = models.TextField(help_text='Bio', default='', blank=True)
    specialty = models.TextField(help_text='Specialties')
    image_sml = models.FileField(
        help_text='Small provider image', upload_to='static/images/providers', default='')
    image = models.FileField(
        help_text='Large provider image', upload_to='static/images/providers', default='')

    class Meta:
        ordering = ['view_order']

    # Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/providers/" + str(self.slug)
        # return reverse('providers:providerDetail', current_app=self.request.resolver_match.namespace, self.slug)


class YoutubeVid(models.Model):
    name = models.CharField(max_length=128)
    video_url = models.URLField()
    provider = models.ForeignKey(
        'Provider',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class CertOrg(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Provider,
        through='CertOrgRelationship',
        through_fields=('certOrg', 'provider')
    )

    def __str__(self):
        return self.name


class CertOrgRelationship(models.Model):
    certOrg = models.ForeignKey(CertOrg, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return self.certOrg.__str__() + " -- " + self.provider.__str__()


class School(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Provider,
        through='SchoolRelationship',
        through_fields=('school', 'provider')
    )

    def __str__(self):
        return self.name


class SchoolRelationship(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    graduation_year = models.IntegerField(
        blank=True, null=True)
    degree = models.TextField(
        help_text='Degree (Optional)', blank=True, default='')

    @ property
    def formatted(self):
        return "<b>" + dict(self.ed_types).get(self.ed_type) + ":</b> " + self.school.__str__()

    # Fields
    ed_types = (
        (1, "College"),
        (2, "Advanced Degree"),
        (3, "Medical School"),
        (4, "Internship"),
        (5, "Residency"),
    )
    ed_type = models.IntegerField(choices=ed_types, default=1)

    def __str__(self):
        return dict(self.ed_types).get(self.ed_type) + ": " + self.school.__str__() + " -- " + self.provider.__str__()
