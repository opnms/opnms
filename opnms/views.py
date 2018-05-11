from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import User,UserGroup
from assets.models import Instance,Server,Container,Node
from business.models import Service


class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['users'] = User.objects.all()
        context['groups'] = UserGroup.objects.all()
        context['instances'] = Instance.objects.all()
        context['servers'] = Server.objects.all()
        context['service'] = Service.objects.all()
        return context