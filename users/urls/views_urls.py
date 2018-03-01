from __future__ import unicode_literals
from django.conf.urls import url
from .. import views
app_name = 'users'

urlpatterns = [
    # login & logout
    url(r'^login',views.UserLoginView.as_view(),name='login'),
    url(r'^logout',views.UserLogoutView.as_view(),name='logout'),
    # user manager
    url(r'^user/$',views.UserListView.as_view(),name='user-list'),
    url(r'^user/create/$',views.UserCreateView.as_view(),name='user-add'),
    url(r'^user/(?P<pk>\d+)/profile/$',views.UserProfileView.as_view(),name='user-profile'),
    url(r'^user/(?P<pk>\d+)/$',views.UserDetailView.as_view(),name='user-detail'),
    url(r'^user/(?P<pk>\d+)/update/$',views.UserInfoUpdateView.as_view(),name='user-update'),
    url(r'^user/(?P<pk>\d+)/delete/$',views.UserDeleteView.as_view(),name='user-delete'),
    # department
    url(r'^department/$',views.DepartmentListView.as_view(),name='department-list'),
    url(r'^department/create/$',views.DepartmentCreateView.as_view(),name='department-add'),
    url(r'^department/(?P<pk>\d+)/update/$',views.DeaprtmentUpdateView.as_view(),name='department-update'),
    url(r'^department/(?P<pk>\d+)/delete/$',views.DepartmentDeleteView.as_view(),name='department-delete'),
    # group
    url(r'^group/create/$',views.GroupCreateView.as_view(),name='group-add'),
    url(r'^group/(?P<pk>\d+)/update/$',views.GroupUpdateView.as_view(),name='group-update'),
    url(r'^group/(?P<pk>\d+)/delete/$',views.GroupDeleteView.as_view(),name='group-delete'),
    #saltapi
    url(r'saltapi/$',views.SaltApiListView.as_view(),name='saltapi-list'),
    url(r'saltapi/create/$',views.SaltApiCreateView.as_view(),name='saltapi-create'),
    url(r'saltapi/(?P<pk>\d+)/update/$',views.SaltApiUpdateView.as_view(),name='saltapi-update'),
]