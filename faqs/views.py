from django.shortcuts import render, redirect
from django.http import Http404
from django.views import generic
from django.views.decorators.cache import cache_page
from django.conf import settings

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
    }

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
    }

    return render(request, 'faqs_index.html', context=context)


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def redirectFAQ(request, old_path):
    faq = FAQ.objects.get(old_path__iexact=old_path)
    return redirect(faq.get_absolute_url(), permanent=True)


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def ob(request):
    return index(request, "1")


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def gyn(request):
    return index(request, "2")


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def postop(request):
    return index(request, "3")
