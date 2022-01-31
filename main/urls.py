# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from casinos import views
from django.conf.urls.i18n import i18n_patterns

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$', views.home, name='home'),
    url('', include('pwa.urls')),
]
urlpatterns += [
    path('admin/clean-positions/', views.clean, name='clean'),
    path('admin/', admin.site.urls),
    path(r'go/<slug:slug>/', views.go, name='go'),
    path(r'<slug:slug>/', views.countries, name='countries'),
]

if settings.DEBUG==True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)