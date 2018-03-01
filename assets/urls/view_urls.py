from __future__ import unicode_literals
from django.conf.urls import url
from .. import views
app_name = 'assets'

urlpatterns = [
    #instance
    url(r'^instance/$',views.InstanceListView.as_view(),name='instance-list'),
    url(r'^instance/(?P<pk>\d+)/$',views.InstanceDetailView.as_view(),name='instance-detail'),
    url(r'^instance/refresh/$',views.InstanceRefreshView.as_view(),name='instance-refresh'),

    #server
    url(r'^server/$',views.ServerListView.as_view(),name='server-list'),
    url(r'^server/(?P<pk>\d+)/$',views.ServerDetailView.as_view(),name='server-detail'),
    url(r'^server/create/$',views.ServerCreateView.as_view(),name='server-create'),
    url(r'^server(?P<pk>)\d+/update/$',views.ServerUpdateView.as_view(),name='server-update'),
    #region
    url(r'^region/$',views.RegionListView.as_view(),name='region-list'),
    url(r'^region/create/$',views.RegionCreateView.as_view(),name='region-create'),
    url(r'^region/(?P<pk>\d+)/update/$',views.RegionUpdateView.as_view(),name='region-update'),
    #cloudprovider
    url(r'^cloud/create/$',views.CloudProviderCreateView.as_view(),name='cloud-create'),
    url(r'^cloud/(?P<pk>\d+)/update/$',views.CloudProviderUpdateView.as_view(),name='cloud-update'),
    url(r'^cloud/(?P<pk>\d+)/delete/$',views.CloudeProviderDeleteView.as_view(),name='cloud-delete'),


]