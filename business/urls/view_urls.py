from __future__ import unicode_literals
from django.conf.urls import url
from .. import views
app_name = 'business'

urlpatterns = [
    url(r'^projects/$',views.ProjectListView.as_view(),name='project-list'),
    url(r'^projects/create/$',views.ProjectCreateView.as_view(),name='project-create'),
    url(r'^projects/(?P<pk>\d+)/detail/$',views.ProjectDetailView.as_view(),name='project-detail'),
    url(r'^projects/(?P<pk>\d+)/create/$',views.ProjectServiceCreateView.as_view(),name='project-service-create'),
    #service
    url(r'^services/$',views.SerivceListView.as_view(),name='service-list'),
]