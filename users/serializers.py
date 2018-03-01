from .models import User,UserGroup,Department
from deploy.models import SaltStack
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','phone','dingding',)


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ('name','comment')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name','comment')

class SaltApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaltStack
        fields = ('url','username','password','comment')