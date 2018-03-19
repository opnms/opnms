from __future__ import unicode_literals

from django.contrib import messages
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect,get_object_or_404,render
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView,DeleteView,FormView
from django.views import View
from django.views.generic.detail import DetailView
from ..models import SaltHost,SaltGroup,SaltModule
from ..forms import SaltGroupForm,SaltHostForm,SaltModuleForm
from ..saltstack import saltapi
import json
from assets.tasks import salt_host_create_update

__all__ = ['SaltHostListView','SaltHostRefreshView','SaltGroupCreateView','SaltGroupUpdateView',
           'SaltModuleListView','SaltGroupDetailView','SaltModuleCreateView','SaltModuleUpdateView',
           'SaltModuleDeployView','SaltGroupListView','SaltDeployModuleView'
           ]

class SaltHostListView(LoginRequiredMixin,TemplateView):
    '''
    salt host and group view.
    '''
    template_name = 'saltstack/salthost_group_list.html'
    model = SaltHost

    def get_context_data(self, **kwargs):
        '''
        get all host and group to salt host list.
        :param kwargs:
        :return: action,salt host and salt group
        '''
        context = super().get_context_data(**kwargs)
        context['action'] = _('Salt Key List')
        context['hostlist'] = SaltHost.objects.all()
        context['modules'] = SaltModule.objects.all()
        return context

class SaltHostRefreshView(SaltHostListView):
    model = SaltHost
    template_name = 'saltstack/salthost_group_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        salt_host_create_update()
        context['hostlist'] = SaltHost.objects.all()
        context['hostgroups'] = SaltGroup.objects.all()
        return context


class SaltGroupCreateView(LoginRequiredMixin,CreateView):
    '''
    salt group create.
    '''
    template_name = 'saltstack/saltgroup_create_update.html'
    model = SaltGroup
    form_class = SaltGroupForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('salt group create')
        context['salthosts'] = SaltHost.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('deploys:salthost-list')


class SaltGroupUpdateView(LoginRequiredMixin,UpdateView):
    '''
    salt group update
    '''
    template_name = 'saltstack/saltgroup_create_update.html'
    model = SaltGroup
    form_class = SaltGroupForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('salt group update')
        context['salthosts'] = SaltHost.objects.all()
        context['saltgroup'] = get_object_or_404(SaltGroup,pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('deploys:salthost-list')

class SaltGroupListView(LoginRequiredMixin,TemplateView):
    '''
    salt group list
    '''

    template_name = 'saltstack/saltgroup_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Salt group list')
        context['hostgroups'] = SaltGroup.objects.all()
        return context



class SaltGroupDetailView(LoginRequiredMixin,DetailView):
    '''
    salt group detail view.
    '''
    model = SaltGroup
    template_name = 'saltstack/saltgroup_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Salt group Detail')
        context['hosts'] = get_object_or_404(SaltGroup,pk=self.kwargs['pk'])
        return context

class SaltModuleListView(LoginRequiredMixin,TemplateView):
    template_name = 'saltstack/saltmodule_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Salt Module List')
        context['modules'] = SaltModule.objects.all()
        return context

class SaltModuleCreateView(LoginRequiredMixin,CreateView):
    '''
    salt module create view.
    '''
    form_class = SaltModuleForm
    model = SaltModule
    template_name = 'saltstack/saltmodule_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Salt Module Create')
        return context

    def form_valid(self, form):
        '''
        save create by.
        :param form:
        :return:
        '''
        saltmodule = form.save(commit=False)
        saltmodule.create_by = self.request.user.username
        saltmodule.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('deploys:salthost-list')



class SaltModuleUpdateView(LoginRequiredMixin,UpdateView):
    '''
    salt module update
    '''
    template_name = 'saltstack/saltmodule_create_update.html'
    model = SaltModule
    form_class = SaltModuleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Salt Module Update')
        context['module'] = get_object_or_404(SaltModule,pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        saltmodule = form.save(commit = False)
        saltmodule.create_by = self.request.user.username
        saltmodule.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('deploys:salthost-list')

class SaltModuleDeployView(LoginRequiredMixin,TemplateView):
    '''
    saltstack deploy module view.
    '''
    template_name = 'saltstack/saltmodule_deploy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Salt Module Deploy')
        context['saltgoups'] = SaltGroup.objects.all()
        context['salthosts'] = SaltHost.objects.all()
        context['modules'] = SaltModule.objects.all()
        return context


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response

class SaltDeployModuleView(LoginRequiredMixin,FormView):
    '''
    salt exec command view,
    '''


    def get(self, request, *args, **kwargs):
        saltgroup = self.request.POST.get('saltgroup')
        return  HttpResponse(saltgroup)

    def post(self,request,*args,**kwargs):
        data = self.request.body
        return HttpResponse(data)
