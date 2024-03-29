from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .models import SysLogin
from datetime import timedelta
from django.contrib.auth.models import User
from sys_auth.models import Role
def json_req(request):
    params = request.POST
    print(params)
    name = params.get('name')
    age = params.get('age')
    print('I am {}, {} years old.'.format(name, age))
    return JsonResponse(
        {'items': [1, 2, 3], 'status': 1, 'message': 'Succeeded!!!'}
    )
def get_roles(request):
    params = request.POST
    username = params.get('username')
    users = User.objects.filter(username__iexact=username)
    if users:
        user = users[0]
        return JsonResponse(
            {'code': 1, 'roles': [('', 'Super Administrator')] if user.is_superuser else [(role.id, role.name) for role in user.role_set.all().order_by('name')]}
        )
    else:
        return JsonResponse(
            {'code': 0}
        )
def do_login(request):
    login_message = ''
    if request.method == 'POST':
        params = request.POST
        username = params.get('username')
        password = params.get('password')
        role_id = params.get('role_id', None)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # 设置session
            request.session['username'] = username                      # 用户账号
            if not user.is_superuser:
                request.session['role_id'] = role_id                    # 非超级管理员设置角色登录角色ID-用于加载对应的菜单
                role = Role.objects.get(pk=role_id)
                request.session['role_name'] = role.name                # 仅做Head显示
                request.session['company_id'] = str(role.company.id)    # 用于数据法人别区分&表单法人过滤
            else:
                request.session['role_name'] = 'Administrator'          # 仅做Head显示
                request.session['company_id'] = ''                      # 用于表单法人过滤
            request.session.set_expiry(timedelta(minutes=30))           # 设置session过期时间-> 30分钟
            # 登录IP地址
            ip = request.META.get('REMOTE_ADDR')
            # 记录登录日志
            login_log = SysLogin(user=user, ip=ip, created_by=user.id, updated_by=user.id)
            login_log.save()
            print('{} authenticate succeeded!!!'.format(username))
            return redirect(reverse('index'))
        else:
            print('Authenticate failed!!!')
            login_message = '认证失败,账号密码有误或账号已停用!'
    return render(request, 'sys_sign/login.html', context=dict(login_message=login_message))
def do_logout(request):
    logout(request)
    return redirect(reverse('sys_sign:login'))
def re_login(request):
    return render(request, 'sys_sign/relogin.html', context={})