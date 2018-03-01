# from django.contrib.auth.models import User
from users.models import User,UserGroup,Department
from deploy.models import SaltStack
from rest_framework import viewsets,permissions
from rest_framework.views import APIView
from .serializers import UserSerializer,UserGroupSerializer,DepartmentSerializer,SaltApiSerializer

from rest_framework.authtoken.models import Token

class UserViewSet(viewsets.ModelViewSet):
    '''
    允许查看和编辑user的api endpoint
    '''

    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class UserToeknView(APIView):
    def post(self):
        user_id = self.request.data.get('user','')

class SaltApiView(viewsets.ModelViewSet):
    queryset = SaltStack.objects.all()
    serializer_class = SaltApiSerializer