from django.shortcuts import render
from django.http import Http404
from django.views.decorators.cache import cache_page
from django.conf import settings

from header.views import renderHeader
from footer.views import renderFooter
from locations.models import Location


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def index(request):

    # Generate counts of some of the main objects
    locations = Location.objects.all()

    context = {
        'locations': locations,
        'headerFragment': renderHeader(request),
        'CANONICAL_PATH': request.build_absolute_uri(request.path),
    }
    context['footerFragment'] = renderFooter(context)

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'locations_index.html', context=context)
