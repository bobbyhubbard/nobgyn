from django.shortcuts import render
from django.http import Http404
from django.views.decorators.cache import cache_page
from django.conf import settings

from locations.models import Location


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def index(request):
    locations = Location.objects.all()

    context = {
        'locations': locations
    }
    return render(request, 'locations_index.html', context=context)
