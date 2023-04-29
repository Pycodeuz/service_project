import time

from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
#
# from apps.client_admin import client_admin_site
# from root import settings
#
# admin.site.site_header = "P8 group"
# admin.site.site_title = "P8 group ning Adminkasi"
# admin.site.index_title = "P8 group saytiga xush kelibsiz!"
#
from django.core.cache import cache


def view(request):
    user_id = request.user.id
    if cache.get(user_id):
        return HttpResponse(user_id)
    cache.set(user_id, request.user.username)
    time.sleep(3)
    return HttpResponse(request.user.username)


urlpatterns = [
    path('data', view),
    path('admin/', admin.site.urls),
    #   path('client-admin/', client_admin_site.urls),
    #   path('', include('apps.urls')),
]  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
