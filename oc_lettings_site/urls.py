from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
