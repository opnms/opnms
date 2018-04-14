"""opnms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve as static_server
from .views import IndexView


urlpatterns = [
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^users/',include('users.urls.views_urls',namespace='users')),
    url(r'^assets/',include('assets.urls.view_urls',namespace='assets')),
    url(r'^captcha/',include('captcha.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^crond/',include('crond.urls.view_urls',namespace='crondtasks')),
    url(r'^deploys/',include('deploy.urls.view_urls',namespace='deploys')),
    url(r'^business/',include('business.urls.view_urls',namespace='business')),

    #api
    url(r'api/assets/',include('assets.urls.api_urls',namespace='api-assets')),
    url(r'api/users/',include('users.urls.view_api',namespace='api-users')),
    url(r'api/crond/',include('crond.urls.api_urls',namespace='api-tasks')),
    url(r'api/deploys/',include('deploy.urls.api_urls',namespace='api-deploys')),
    url(r'api/business/',include('business.urls.api_urls',namespace='api-business')),
]




urlpatterns += [

] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)