from rest_framework import serializers
from .models import LikeAndComplain
from login.serializers import UserDescSerializer, UserSerializer


class ComplainSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="likeandcomplain-detail", lookup_field="id")
    # 嵌套关系字段
    author = UserDescSerializer(read_only=True)

    class Meta:
        model = LikeAndComplain
        fields = [
            'url',
            'id',
            'author',
            'title',
            'content',
            'data_time',
            'score',
        ]