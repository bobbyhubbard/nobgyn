from django.shortcuts import render
from django.template.loader import get_template
from providers.models import Provider
from services.models import Service
from resources.models import Resource
from locations.models import Location


def renderFooter(context):

    providers = Provider.objects.filter(doctor=True)
    services = Service.objects.all()
    resources = Resource.objects.all()
    locations = Location.objects.all()
    context = {
        'providers': providers,
        'resources': resources,
        'services': services,
        'locations': locations,
    }

    template = get_template("footer.html")

    return template.render(context)
