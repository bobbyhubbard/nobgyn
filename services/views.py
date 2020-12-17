from django.shortcuts import render
from django.http import Http404
from django.views import generic
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.conf import settings

from services.models import Service
from header.views import renderHeader
from footer.views import renderFooter


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def serviceDetail(request, slug):
    try:
        service = Service.objects.get(slug__iexact=slug)
    except Service.DoesNotExist:
        raise Http404("Sorry, this page does not exist. ")

    context = {
        'service': service,
        'headerFragment': renderHeader()
    }
    context['footerFragment'] = renderFooter(context)

    if (slug == "massage-therapy"):
        return render(request, 'service_massage.html', context=context)
    else:
        return render(request, 'service_detail.html', context=context)


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def index(request):
    services = Service.objects.all()

    context = {
        'services': services,
        'headerFragment': renderHeader()
    }
    context['footerFragment'] = renderFooter(context)

    return render(request, 'services_index.html', context=context)
