from django.conf import settings
from header.views import renderHeader
from footer.views import renderFooter


def global_settings(request):
    # return any necessary values
    return {
        'G_TAG_ID': settings.G_TAG_ID,
        'GOOGLE_API_KEY': settings.GOOGLE_API_KEY,
        'headerFragment': renderHeader(request),
        'CANONICAL_PATH': request.build_absolute_uri(request.path),
        'footerFragment': renderFooter(None)
    }
