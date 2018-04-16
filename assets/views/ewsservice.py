from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.detail import DetailView
from ..models import Host,Container,Node,Image
from ..forms import ServerForm

__all__ = ['ContainerListView','NodeListVew','ImageListVew','HostListVew']

class ContainerListView(LoginRequiredMixin,TemplateView):
    model = Container
    template_name = 'ewsservice/container_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('containerList')
        context['containers'] = Container.objects.all()
        return context

class NodeListVew(LoginRequiredMixin,TemplateView):
    model = Node
    template_name = 'ewsservice/node_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('nodeList')
        context['nodes'] = Node.objects.all()
        return context


class ImageListVew(LoginRequiredMixin,TemplateView):
    model = Image
    template_name = 'ewsservice/image_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('imageList')
        context['images'] = Image.objects.all()
        return context


class HostListVew(LoginRequiredMixin,TemplateView):
    model = Host
    template_name = 'ewsservice/host_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('imageList')
        context['hosts'] = Host.objects.all()
        return context