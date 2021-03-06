"""Main URLs module."""

from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

    # patyh('', include('cride.circles.urls', 'circles'), namespace='circles'),
    # patyh('', include('cride.users.urls', 'users'), namespace='users'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
