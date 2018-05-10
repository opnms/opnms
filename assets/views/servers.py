from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.detail import DetailView
from ..models import Region,Cloudprovider,Instance,Server,Host,Container
from ..forms import ServerForm

__all__ = ['ServerListView','ServerDetailView','ServerCreateView','ServerUpdateView']

class ServerListView(LoginRequiredMixin,TemplateView):
    model = Server
    template_name = 'server/server_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Server List')
        context['servers'] = Server.objects.all()
        return context

class ServerDetailView(LoginRequiredMixin,DetailView):
    model = Server
    template_name = 'server/server_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Server Detail')
        context['serverinfo'] = get_object_or_404(Server,pk=self.kwargs['pk'])
        instance = Server.objects.get(pk=self.kwargs['pk'])

        context['hosts'] = get_object_or_404(Host,instanceId = instance.instanceid)
        host = get_object_or_404(Host,instanceId = instance.instanceid)
        print(host.id)
        context['containers'] = Container.objects.all().filter(hostId=host.id)
        return context

class ServerCreateView(LoginRequiredMixin,CreateView):
    model = Server
    template_name = 'server/server_create_update.html'
    form_class = ServerForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Server Create')
        return context

    def form_valid(self, form):
        server = form.save(commit=False)
        server.create_by = self.request.user.username
        server.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('assets:server-detail')

class ServerUpdateView(LoginRequiredMixin,UpdateView):
    model = Server
    form_class = ServerForm
    template_name = 'server/server_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Server Update')
        context['server'] = get_object_or_404(Server,pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        server = form.save(commit=False)
        server.create_by = self.request.user.username
        server.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('assets:server-detail')