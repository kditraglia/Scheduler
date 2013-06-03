from django.conf.urls.defaults import *
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
  (r'^view', 'main.views.view'),
  (r'^admin/', include(admin.site.urls)),
    url(
      r'^show_appointment/(?P<slug>[^\.]+)',
      'main.views.show_appointment',
      name='show_appointment'),
)
