from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from .models import User
from . import form

# djangorestframe
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


def index(request):
    pass
    return render(request, 'login/index.html', locals())


class LoginAndRegViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "name"
    rep = {'message': "请检查填写的内容"}


def logout(request):
    if not request.session.get('is_login', None):
        return redirect("login:loginAndRegister")

    request.session.flush()
    return redirect("login:loginAndRegister")
