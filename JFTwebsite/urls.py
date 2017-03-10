from django.conf.urls import url,include
from django.conf import settings
from JFTwebsite.views import brushuppages,download_CV,cvcredits
from jftcv.views import cv
import django
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^([A-Za-z]*)/$', cv),
    url(r'^BrushUp/([A-Za-z]*)/$', brushuppages),
    url(r'^CVOnline/home/$', cvcredits),
    url(r'^admin1/', include(admin.site.urls)),
    url(r'^download_CV/([A-Za-z]*)/$', download_CV),

]

if settings.DEBUG:
  urlpatterns.append(url(r'^([A-Za-z]*.png)/$', django.views.static.serve,{'document_root': settings.MEDIA_ROOT}))
  urlpatterns.append(url(r'^([A-Za-z]*.png)/$', django.views.static.serve,{'document_root': settings.STATIC_ROOT}))
  urlpatterns.append(url(r'^[A-Za-z]*/([A-Za-z]*.png)/$', django.views.static.serve,{'document_root': settings.MEDIA_ROOT}))
  urlpatterns.append(url(r'^[A-Za-z]*/([A-Za-z]*.png)/$', django.views.static.serve,{'document_root': settings.STATIC_ROOT}))

