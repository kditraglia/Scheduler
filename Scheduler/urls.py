from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  (r'^$', 'main.views.index'),
  (r'^about', 'main.views.about'),
  (r'^directions', 'main.views.directions'),
  (r'^appointment', 'main.views.appointment'),
  (r'^admin/', include(admin.site.urls)),
)
