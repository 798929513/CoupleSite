from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user-detail", lookup_field="name")

    class Meta:
        model = User
        fields = [
            'url',
            'id',
            'name',
            'password',
            'email',
            'sex',
            'lover',
            'create_time'
        ]


class UserDescSerializer(serializers.ModelSerializer):
    """在吐槽牢骚列表中引用的嵌套序列化器"""

    class Meta:
        model = User
        fields = [
            'name',
            'lover',
            'sex'
        ]