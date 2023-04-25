from django.urls import path

from apps.views import view

urlpatterns = [
    path('view', view)
]

