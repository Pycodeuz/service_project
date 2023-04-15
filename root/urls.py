from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.client_admin import client_admin_site
from root import settings

admin.site.site_header = "P8 group"
admin.site.site_title = "P8 group ning Adminkasi"
admin.site.index_title = "P8 group saytiga xush kelibsiz!"

urlpatterns = [
  path('admin/', admin.site.urls),
  path('client-admin/', client_admin_site.urls),
  path('', include('apps.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
