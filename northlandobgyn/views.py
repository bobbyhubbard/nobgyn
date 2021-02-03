from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.conf import settings

from providers.models import Provider
from services.models import Service
from locations.models import Location
from resources.models import Resource


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def index(request):
    providers = Provider.objects.filter(doctor=True)
    services = Service.objects.all()
    locations = Location.objects.all()
    resources = Resource.objects.all()

    context = {
        'providers': providers,
        'services': services,
        'locations': locations,
        'resources': resources
    }

    return render(request, 'index.html', context=context)


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def terms(request):
    return render(request, 'terms.html')


def page_not_found(request, exception):
    return render(request, '404.html', status=404)


def server_error(request):
    return render(request, '500.html', status=500)
