from django.shortcuts import render, redirect

from rest_framework.viewsets import ModelViewSet

from login.models import User
from featureArea.models import LikeAndComplain
from featureArea.serializers import ComplainSerializer



# Create your views here.

def things(request):
    pass
    return render(request, 'featureArea/things.html', locals())


def love_list(request):
    pass
    return render(request, 'featureArea/love_list.html', locals())


class LikeAndComplainViewSet(ModelViewSet):
    queryset = LikeAndComplain.objects.all()
    serializer_class = ComplainSerializer
    lookup_field = "id"

    def perform_create(self, serializer):
        request_user = User.objects.filter(name=self.request.data['author']['name'])
        if request_user[0]:
            serializer.save(author=request_user[0])
