from django.shortcuts import render
from django.template.loader import get_template
from header.models import Banner
from django.utils import timezone


def renderHeader():
    banners = Banner.objects.filter(publish_date__lte=timezone.now()).filter(
        expiration_date__gte=timezone.now())

    context = {
        'banners': banners
    }
    template = get_template("header.html")

    return template.render(context)
