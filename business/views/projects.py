from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.detail import DetailView
from ..models import Project,ProjectEnv,Service
from users.models import User
from ..forms import ProjectForm,ProjectServiceForm


__all__ = ['ProjectListView','ProjectCreateView','ProjectDetailView','ProjectServiceCreateView']

class ProjectListView(LoginRequiredMixin,TemplateView):
    template_name = 'projects/project_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Project List')
        context['projects'] = Project.objects.all()
        return context

class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    template_name = 'projects/project_create_update.html'
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Project Create')
        context['users'] = User.objects.all()
        return context

    def form_valid(self, form):
        project = form.save(commit=False)
        project.create_by = self.request.user.username
        project.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('business:project-list')

class ProjectDetailView(LoginRequiredMixin,DetailView):
    model = Project
    template_name = 'projects/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('Project Detail')
        context['project'] = get_object_or_404(Project,pk=self.kwargs['pk'])
        context['services'] = ProjectEnv.objects.filter(project=self.kwargs['pk'])
        return context

class ProjectServiceCreateView(LoginRequiredMixin,CreateView):
    form_class = ProjectServiceForm
    template_name = 'projects/project_service_create_update.html'
    model = ProjectEnv

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _('project create service')
        context['projects'] = get_object_or_404(Project,pk=self.kwargs['pk'])
        context['pk'] = self.kwargs['pk']
        context['services'] = Service.objects.all().order_by('name')
        return context

    def form_valid(self, form):
        projectenv = form.save(commit=False)
        projectenv.project = get_object_or_404(Project,pk=self.kwargs['pk'])
        projectenv.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('business:project-detail',kwargs={'pk':self.kwargs['pk']})
