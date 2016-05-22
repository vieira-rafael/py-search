from django.conf.urls import patterns, include, url
from django.contrib import adminadmin.autodiscover()
urlpatterns = [    url(r'^admin/', include(admin.site.urls)),]