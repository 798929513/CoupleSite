from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from .models import User
from . import form


def index(request):
    pass
    return render(request, 'login/index.html', locals())


# 登录和注册页面
def login_and_register(request):
    # 已经登录就不要再注册或者登录了
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == "POST":
        if 'login' in request.POST:
            login_form = form.LoginForm(request.POST)
            register_form = form.RegisterForm()
            message = "请检查填写的内容"
            if login_form.is_valid():
                username_login = login_form.cleaned_data.get('username_login')
                password_login = login_form.cleaned_data.get('password_login')
                try:
                    user = User.objects.get(name=username_login)
                except:
                    message = "用户不存在"
                    return render(request, 'login/loginAndRegister.html', locals())

                if password_login == user.password:
                    # 记录会话信息
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name

                    return redirect('/index/')
                else:
                    message = "密码错误"
                    return render(request, 'login/loginAndRegister.html', locals())
            else:
                return render(request, 'login/loginAndRegister.html', locals())
        if 'register' in request.POST:
            login_form = form.LoginForm()
            register_form = form.RegisterForm(request.POST)

            message = "请检查填写的内容"
            if register_form.is_valid():
                # 获取 注册 信息
                username_register = register_form.cleaned_data.get('username_register')
                email = register_form.cleaned_data.get('email')
                password_register = register_form.cleaned_data.get('password_register')
                confirm_pass = register_form.cleaned_data.get('confirm_pass')

                # 两次输入密码不一样
                if password_register != confirm_pass:
                    message = "两次输入密码不一致"
                    return render(request, 'login/loginAndRegister.html', locals())

                # 用户名已经存在
                same_name_user = User.objects.filter(name=username_register)
                if same_name_user:
                    message = "用户名已经存在"
                    return render(request, 'login/loginAndRegister.html', locals())

                # 邮箱已经被注册
                same_email_user = User.objects.filter(email=email)
                if same_email_user:
                    message = "邮箱已经被注册"
                    return render(request, 'login/loginAndRegister.html', locals())

                # 注册成功，进行保存
                message = "注册成功"
                new_user = User()
                new_user.name = username_register
                new_user.email = email
                new_user.password = password_register
                new_user.save()
                return render(request, 'login/loginAndRegister.html', locals())
            else:
                return render(request, 'login/loginAndRegister.html', locals())
    else:
        login_form = form.LoginForm()
        register_form = form.RegisterForm()
        return render(request, 'login/loginAndRegister.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect("login:loginAndRegister")

    request.session.flush()
    return redirect("login:loginAndRegister")
