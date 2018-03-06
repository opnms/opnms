from __future__ import unicode_literals
from django.conf.urls import url
from .. import views
app_name = 'deploy'

urlpatterns = [
    #salt host
    url(r'^salthost/$',views.SalstHostListView.as_view(),name='salthost-list'),
    url(r'^salthost/create/$',views.SaltHostCreateView.as_view(),name='salthost-create'),

    #salt group
    url(r'^salt-group/create/$',views.SaltGroupCreateView.as_view(),name='saltgroup-create'),
    url(r'^salt-group/(?P<pk>\d+)/update/$',views.SaltGroupUpdateView.as_view(),name='saltgroup-update'),
    ]