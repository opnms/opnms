from rest_framework import routers,viewsets
from ..models import SaltGroup,SaltHost
from ..serializers import SaltHostSerializer,SaltGroupSerializer


__all__ = ['SaltHostViewSet','SaltGroupViewSet']

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



class SaltGroupViewSet(viewsets.ModelViewSet):
    queryset = SaltGroup.objects.all()
    serializer_class = SaltGroupSerializer