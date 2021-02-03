from django.shortcuts import render
from django.template.loader import get_template
from header.models import Banner
from django.utils import timezone
from django.urls import resolve


def renderHeader(request):
    banners = Banner.objects.filter(publish_date__lte=timezone.now()).filter(
        expiration_date__gte=timezone.now())
    prefex = ""
    try:
        prefex = resolve(request.path).app_name
    except:
        # do Nothing
        print("")

    context = {
        'banners': banners,
        'isActive_' + prefex: 'active'
    }
    template = get_template("header.html")
    return template.render(context)
