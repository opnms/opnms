from __future__ import unicode_literals
from django.conf.urls import url
from .. import views
app_name = 'crondtask'


urlpatterns = [
    #instance
    url(r'^periodic/$',views.PeriodicTasksListView.as_view(),name='periodic-list'),

    #crontab
    url(r'^crontab/$',views.CrontabListView.as_view(),name='crontab-list'),
    url(r'^crontab/create/$',views.CrontabCreateView.as_view(),name='crontab-create'),
    url(r'^crontab/(?P<pk>\d+)/update/$',views.CrontabUpdateView.as_view(),name='crontab-update'),

    #interval
    url(r'^interval/create/$',views.IntervalCreateView.as_view(),name='interval-create'),
    url(r'^interval/(?P<pk>\d+)/update/$',views.IntervalUpdateView.as_view(),name='interval-update'),

    #solar
    # url(r'^solar/create/$',views.SolarCreateView.as_view(),name='solar-create'),
    # url(r'^solar/(?P<pk>)\d+/update/$',views.SolarUpdateView.as_view(),name='solar-update'),

    ]