# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render, redirect
from autotest import models

user_list = []
def index(request):
    # return HttpResponse(u"欢迎光临 自动化测试平台!")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        # temp = {'user':username,'pwd':password}
        # user_list.append(temp)

        # 将数据保存到数据库
        models.UserInfo.objects.create(user=username,pwd=password)

    # 从数据库中读取数据
    user_list = models.UserInfo.objects.all()
    return render(request,'index.html', {'data':user_list})


def login(request):
    if request.method == 'POST':  # 如果为post请求，判断用户名密码是否正确
        username = request.POST.get('username')
        password = request.POST.get('password')
        pwd = models.UserInfo.objects.filter(user=username)
        if password == pwd:  # 如果用户名密码匹配
            obj = redirect('/index/')   # 跳转index页面
            obj.set_cookie('c_user',username)   # 将用户名写入cookie中
            return redirect('/index/')
        else:   # 如果用户名密码不匹配，加载login.html
            return render(request,'login.html')
    else:   # 如果为get请求，判断是否已经登录
        c_user = request.COOKIES.get('c_user')
        if not c_user:   # 未登录留在登录页面
            return render(request, 'login.html')
        else:   # 已登录进入index
            return redirect('/index/')



    user = request.COOKIES.get('username')
    if not user:
        return redirect('/login/')
    else:
        return redirect('/index/')



confs=[]
def conf(request):
    # 更新配置
    if request.method == 'POST':
        rule = request.POST.get('rule')
        api_data = request.POST.get('api_data')
        api_report = request.POST.get('api_report')
        process_data = request.POST.get('process_data')
        process_report = request.POST.get('process_report')
        smtp_host = request.POST.get('smtp_host')
        from_addr = request.POST.get('from_addr')
        password = request.POST.get('password')
        to_addr = request.POST.get('to_addr')
        confs ={'username':'admin',
                'rule':rule,
                'api_data':api_data,
                'api_report':api_report,
                'process_data':process_data,
                'process_report':process_report,
                'smtp_host':smtp_host,
                'from_addr':from_addr,
                'password':password,
                'to_addr':to_addr}
        # print('匹配的数据条数为：',models.Confs.objects.filter(username=confs.get('username')).count())
        if models.Confs.objects.filter(username=confs.get('username')).count() == 0:
            # 如果没有数据，insert
            models.Confs.objects.create(**confs)
        else:
            # 如果已有数据，更新之
            models.Confs.objects.filter(username=confs.get('username')).update(**confs)

        print('数据总条数为：',models.Confs.objects.count())
        # res = models.Confs.objects.all()
        # for i in res:
        #     print(i.rule)
    return render(request,'conf.html')




 # models.Confs.objects.create(rule=rule,
            #                             api_data=api_data,
            #                             api_report=api_report,
            #                             process_data=process_data,
            #                             process_report=process_report,
            #                             smtp_host=smtp_host,
            #                             from_addr=from_addr,
            #                             password=password,
            #                             to_addr=to_addr)