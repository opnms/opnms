from __future__ import unicode_literals
from django.conf.urls import url
from .. import views
app_name = 'deploy'

urlpatterns = [
    #instance
    url(r'^salthost/$',views.SalstHostListView.as_view(),name='salthost-list'),
    ]