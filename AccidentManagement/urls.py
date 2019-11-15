from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('dashboard/', include('dashboard.urls')),
    path('accitracker/', include('acciTracker.urls')),
]
