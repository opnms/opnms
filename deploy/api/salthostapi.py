from rest_framework import routers,viewsets
from rest_framework import generics
from ..models import SaltGroup,SaltHost,SaltModule
from ..serializers import SaltHostSerializer,SaltGroupSerializer,SaltModuleSerializer


__all__ = ['SaltHostViewSet','SaltGroupViewSet','SaltModuleViewset','SaltHostListApi']

class SaltHostViewSet(viewsets.ModelViewSet):
    queryset = SaltHost.objects.all()
    serializer_class = SaltHostSerializer

    def get_queryset(self):
        '''
        query minion,if exist do update,else post it.
        :return:
        '''
        queryset = super(SaltHostViewSet,self).get_queryset()
        minion = self.request.query_params.get('minion',None)
        if minion is not None:
            queryset = queryset.filter(minion=minion)
        return queryset

class SaltHostListApi(generics.ListAPIView):
    queryset = SaltHost.objects.all()
    serializer_class = SaltHostSerializer

    def get_queryset(self,*args,**kwargs):
        queryset = super().get_queryset()
        minion_id = self.kwargs['pk']
        if id is not None:
            queryset = queryset.filter(id=minion_id)

        return queryset




class SaltGroupViewSet(viewsets.ModelViewSet):
    queryset = SaltGroup.objects.all()
    serializer_class = SaltGroupSerializer

class SaltModuleViewset(viewsets.ModelViewSet):
    queryset = SaltModule.objects.all()
    serializer_class = SaltModuleSerializer