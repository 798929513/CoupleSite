from django.shortcuts import render, redirect

from login.models import User
from featureArea.models import LikeAndComplain


# Create your views here.


def things(request):
    pass
    return render(request, 'featureArea/things.html', locals())


def love_list(request):
    pass
    return render(request, 'featureArea/love_list.html', locals())


def like_and_complain(request):
    # 判断是否登录
    if request.session.get('is_login', None):
        # 登录了
        # 就获取登录人的信息
        username = request.session['user_name']
        # 找到登录者
        user = User.objects.filter(name=username).first()
        # 根据登录者的name，找到他的lover
        user_lover = User.objects.filter(lover__name=username).first()
        if user_lover:
            # 找到双方对对方的评论
            # 登录者对对方的评论
            user_comment_list = LikeAndComplain.objects.filter(author=user)
            # 登陆者爱人对自己的评论
            lover_comment_list = LikeAndComplain.objects.filter(author=user_lover)
            return render(request, 'featureArea/like_and_complain.html', locals())
        else:
            message = "您还没有进行情侣绑定"
            return render(request, 'featureArea/like_and_complain.html', locals())
    else:
        message = "您没有登录"
        return render(request, 'featureArea/like_and_complain.html', locals())