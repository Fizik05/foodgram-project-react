from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("users.urls", namespace="users")),
    path("api/", include("api.urls", namespace="api")),
]

if settings.DEBUG:
    urlpatterns = (
        urlpatterns +
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
