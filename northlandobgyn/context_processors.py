from django.conf import settings


def global_settings(request):
    # return any necessary values
    return {
        'GOOGLE_ANALYTICS': settings.G_TAG_ID,
        'GOOGLE_API_KEY': settings.GOOGLE_API_KEY
    }
