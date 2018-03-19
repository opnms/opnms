from __future__ import unicode_literals
from django.conf.urls import url
from .. import views
app_name = 'deploy'

urlpatterns = [
    #salt host
    url(r'^salthost/$',views.SaltHostListView.as_view(),name='salthost-list'),
    url(r'^salthost/refresh/$',views.SaltHostRefreshView.as_view(),name='salthost-refresh'),

    #salt module
    url(r'^saltmodule/$',views.SaltModuleListView.as_view(),name='saltmodule-list'),
    url(r'^saltmodule/create/$',views.SaltModuleCreateView.as_view(),name='saltmodule-create'),
    url(r'^saltmodule/(?P<pk>\d+)/update/$',views.SaltModuleUpdateView.as_view(),name='saltmodule-update'),
    url(r'^saltmodule/deploy/$', views.SaltModuleDeployView.as_view(), name='saltmodule-deploy'),

    #salt group
    url(r'^salt-group/$',views.SaltGroupListView.as_view(),name='saltgroup-list'),
    url(r'^salt-group/create/$',views.SaltGroupCreateView.as_view(),name='saltgroup-create'),
    url(r'^salt-group/(?P<pk>\d+)/update/$',views.SaltGroupUpdateView.as_view(),name='saltgroup-update'),
    url(r'^saltgroup/(?P<pk>\d+)/detail/$',views.SaltGroupDetailView.as_view(),name='saltgroup-detail'),

    #salt deploy
    url(r'^salt-deploy/module/$',views.SaltDeployModuleView.as_view(),name='salt-module-deploy'),
    ]