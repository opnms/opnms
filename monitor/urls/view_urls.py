from __future__ import unicode_literals
from django.conf.urls import url
from .. import views
app_name = 'monitor'

urlpatterns = [
    url(r'^http/$',views.HttpMonitorListView.as_view(),name='monitor-http-list'),
    url(r'http/create/$',views.HttpMonitorCreateView.as_view(),name='monitor-http-create'),
    url(r'http/(?P<pk>\d+)/update/$',views.HttpMonitorUpdateView.as_view(),name='monitor-http-update'),
]