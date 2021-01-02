from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.conf import settings

from providers.models import Provider
from services.models import Service
from header.views import renderHeader
from footer.views import renderFooter
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
        'resources': resources,
        'headerFragment': renderHeader(request),
        'CANONICAL_PATH': request.build_absolute_uri(request.path),
    }
    context['footerFragment'] = renderFooter(context)

    return render(request, 'index.html', context=context)


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def terms(request):
    context = {
        'headerFragment': renderHeader(request),
        'CANONICAL_PATH': request.build_absolute_uri(request.path),
    }
    context['footerFragment'] = renderFooter(context)

    return render(request, 'terms.html', context=context)
