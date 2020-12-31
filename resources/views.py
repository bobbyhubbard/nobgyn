from django.shortcuts import render
from django.http import Http404
from string import ascii_lowercase
from django.views.decorators.cache import cache_page
from django.conf import settings

from header.views import renderHeader
from footer.views import renderFooter
from resources.models import Resource, Form, FAQLink, Info, HealthPlan


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def forms_information(request):
    try:
        resource = Resource.objects.get(slug__iexact="forms_information")
        forms = Form.objects.all()
        faqs = FAQLink.objects.all()
        infos = Info.objects.all()

    except Resource.DoesNotExist:
        raise Http404("Sorry, this page does not exist. ")

    context = {
        'resource': resource,
        'forms': forms,
        'faqs': faqs,
        'infos': infos,
        'headerFragment': renderHeader(),
        'CANONICAL_PATH': request.build_absolute_uri(request.path),
    }
    context['footerFragment'] = renderFooter(context)

    return render(request, 'forms_information.html', context=context)


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def health_plans(request):
    try:
        resource = Resource.objects.get(slug__iexact="health_plans")
        _plans = HealthPlan.objects.all()

    except Resource.DoesNotExist:
        raise Http404("Sorry, this page does not exist. ")

    plans = {}

    for plan in _plans:
        firstLetter = plan.name[0]
        if plans.get(firstLetter):
            letterPlans = plans.get(firstLetter)
            letterPlans.append(plan.name)
        else:
            plans.update({firstLetter: [plan]})

    context = {
        'resource': resource,
        'plans': plans,
        'headerFragment': renderHeader(),
        'CANONICAL_PATH': request.build_absolute_uri(request.path),
    }
    context['footerFragment'] = renderFooter(context)

    return render(request, 'health_plans.html', context=context)


@cache_page(settings.CACHE_VIEW_EXPIRATION)
def index(request):

    resources = Resource.objects.all()
    forms = Form.objects.all()
    faqs = FAQLink.objects.all()
    infos = Info.objects.all()

    context = {
        'resources': resources,
        'forms': forms,
        'faqs': faqs,
        'infos': infos,
        'headerFragment': renderHeader(),
        'CANONICAL_PATH': request.build_absolute_uri(request.path),
    }
    context['footerFragment'] = renderFooter(context)

    return render(request, 'resources_index.html', context=context)
