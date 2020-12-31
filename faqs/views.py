from django.shortcuts import render
from django.http import Http404
from django.views import generic
from django.views.decorators.cache import cache_page
from django.conf import settings

from header.views import renderHeader
from footer.views import renderFooter
from faqs.models import FAQ


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def faqDetail(request, slug):
    try:
        faq = FAQ.objects.get(slug__iexact=slug)
    except Service.DoesNotExist:
        # handle redirect here for old paths?
        raise Http404("Sorry, this FAQ does not exist. ")

    context = {
        'faq': faq,
        'headerFragment': renderHeader(),
        'CANONICAL_PATH': request.build_absolute_uri(request.path),
    }
    context['footerFragment'] = renderFooter(context)

    return render(request, 'faq_detail.html', context=context)


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def index(request, type="1"):
    if type:
        faqs = FAQ.objects.filter(faq_type=type)
    else:
        faqs = FAQ.objects.all()

    context = {
        'faqs': faqs,
        'type': FAQ.faqTypeName(type),
        'headerFragment': renderHeader(),
        'CANONICAL_PATH': request.build_absolute_uri(request.path),
    }
    context['footerFragment'] = renderFooter(context)

    return render(request, 'faqs_index.html', context=context)


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def ob(request):
    return index(request, "1")


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def gyn(request):
    return index(request, "2")


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def postop(request):
    return index(request, "3")
