from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from chains import views

urlpatterns = patterns('',
                       url(r'^chains/$',
                           views.ChainList.as_view()),

                       url(r'^chains/(?P<pk>[0-9]+)/$',
                           views.ChainDetail.as_view()),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)
