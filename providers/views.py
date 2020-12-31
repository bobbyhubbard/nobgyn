from django.shortcuts import render
from django.http import Http404
from django.views.decorators.cache import cache_page
from django.conf import settings

from header.views import renderHeader
from footer.views import renderFooter
from providers.models import Provider, SchoolRelationship, CertOrgRelationship, YoutubeVid


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def providerDetail(request, slug):
    try:
        provider = Provider.objects.get(slug__iexact=slug)
        schoolRels = SchoolRelationship.objects.filter(
            provider__slug__iexact=slug)
        certOrgRels = CertOrgRelationship.objects.filter(
            provider__slug__iexact=slug)
        vids = YoutubeVid.objects.filter(
            provider__slug__iexact=slug)
    except Provider.DoesNotExist:
        raise Http404("Sorry, this page does not exist. ")

    context = {
        'provider': provider,
        'schoolRels': schoolRels,
        'certOrgRels': certOrgRels,
        'vids': vids,
        'headerFragment': renderHeader(),
        'CANONICAL_PATH': request.build_absolute_uri(request.path),
    }
    context['footerFragment'] = renderFooter(context)

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'provider_detail.html', context=context)


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def index(request):

    # Generate counts of some of the main objects
    providers = Provider.objects.all()

    context = {
        'providers': providers,
        'headerFragment': renderHeader(),
        'CANONICAL_PATH': request.build_absolute_uri(request.path),
    }
    context['footerFragment'] = renderFooter(context)

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'providers_index.html', context=context)
