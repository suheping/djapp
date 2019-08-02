# coding:utf-8

import os
import random
import time
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render
from autotest import models
from bin import run

user_list = []
def index(request):
    # 获取令牌
    ticket = request.COOKIES.get('ticket')
    if not ticket:  # 如果cookie中没有ticket
        return HttpResponseRedirect('/login/') # 重定向到登录页面
    else:
        if models.UserInfo.objects.filter(ticket=ticket).exists():  # 如果有匹配的ticket
            return render(request,'index.html',{'name': models.UserInfo.objects.filter(ticket=ticket)[0].user})
        else:   # 如果没有匹配的ticket
            return HttpResponseRedirect('/login/')


def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        c_passwd = request.POST.get('c_passwd')

        if password != c_passwd:
            return HttpResponse('密码输入不一致！')
        else:
            if models.UserInfo.objects.filter(user=username).count() == 0:
                models.UserInfo.objects.create(user=username, pwd=make_password(password))
                return HttpResponseRedirect('/login/')
            else:
                return HttpResponse('用户名已存在')
    else:
        return render(request,'reg.html')


def login(request):
    if request.method == 'GET':
        print('截获登录get请求')
        # 获取令牌
        ticket = request.COOKIES.get('ticket')
        if not ticket:  # 如果cookie中没有ticket
            return render(request,'login.html')  # 重定向到登录页面
        else:
            if models.UserInfo.objects.filter(ticket=ticket).exists():  # 如果有匹配的ticket
                return render(request,'index.html',{'name': models.UserInfo.objects.filter(ticket=ticket)[0].user})
            else:  # 如果没有匹配的ticket
                return HttpResponseRedirect('/login/')
    else:
        print('截获登录请求')
        name = request.POST.get('username')
        password = request.POST.get('password')
        if models.UserInfo.objects.filter(user=name).exists(): #判断用户名是否存在
            user = models.UserInfo.objects.get(user=name)
            if check_password(password,user.pwd):  # 判断密码是否正确
                ticket =''
                for i in range(16):
                    s = 'abcdefghijklmnopqrstuvwxyz'
                    ticket += random.choice(s)
                now_time = int(time.time())
                ticket = 'TK'+ticket+str(now_time)
                print('ticket: ' + ticket)
                # 绑定令牌到cookie中
                response = HttpResponseRedirect('/index/')
                response.set_cookie('ticket',ticket,max_age= 300)
                # 将令牌存在服务端
                user.ticket = ticket
                user.save()
                return response
            else:
                # return render(request,'login.html',{'password':'用户密码错误'})
                return HttpResponse('密码错误')
        else:
            # return render(request,'login.html',{'name':'用户不存在'})
            return HttpResponse('用户不存在')


def logout(request):
    response = HttpResponseRedirect('/login/')
    response.set_cookie('ticket','',max_age=0)
    return response


def uploadConf(request):
    if request.method == 'POST':
        confFile = request.FILES.get("conf_file")
        if not confFile:
            return HttpResponse("请选择配置文件后上传")
        else:
            # 获取令牌
            ticket = request.COOKIES.get('ticket')
            username = models.UserInfo.objects.filter(ticket=ticket)[0].user
            user_path = os.path.join("conf/" + username + '/')
            if not os.path.exists(user_path):
                os.mkdir(user_path)
            dest = open(os.path.join(user_path, 'config.conf'), 'wb+')
            for chunk in confFile.chunks():
                dest.write(chunk)
            dest.close()
            return HttpResponse('上传完成')
    else:
        # 获取令牌
        ticket = request.COOKIES.get('ticket')
        if not ticket:  # 如果cookie中没有ticket
            return HttpResponseRedirect('/login/')  # 重定向到登录页面
        else:
            if models.UserInfo.objects.filter(ticket=ticket).exists():  # 如果有匹配的ticket
                return render(request, 'uploadConf.html',{'name': models.UserInfo.objects.filter(ticket=ticket)[0].user})
            else:  # 如果没有匹配的ticket
                return HttpResponseRedirect('/login/')


def uploadDatafile(request):
    if request.method == 'POST':
        dataFile = request.FILES.get("datafile")
        if not dataFile:
            return HttpResponse("请选择测试用例文件后上传")
        else:
            # 获取令牌
            ticket = request.COOKIES.get('ticket')
            username = models.UserInfo.objects.filter(ticket=ticket)[0].user
            user_path = os.path.join("data/" + username + '/')
            if not os.path.exists(user_path):
                os.mkdir(user_path)
            dest = open(os.path.join(user_path,dataFile.name),'wb+')
            for chunk in dataFile.chunks():
                dest.write(chunk)
            dest.close()
            return HttpResponse('上传完成')
    else:
        # 获取令牌
        ticket = request.COOKIES.get('ticket')
        if not ticket:  # 如果cookie中没有ticket
            return HttpResponseRedirect('/login/')  # 重定向到登录页面
        else:
            if models.UserInfo.objects.filter(ticket=ticket).exists():  # 如果有匹配的ticket
                return render(request,'uploadDatafile.html',{'name': models.UserInfo.objects.filter(ticket=ticket)[0].user})
            else:  # 如果没有匹配的ticket
                return HttpResponseRedirect('/login/')


def runtest(request):
    if request.method == 'POST':
        print('截获post请求')
        # 获取令牌
        ticket = request.COOKIES.get('ticket')
        if not ticket:  # 如果cookie中没有ticket
            return HttpResponseRedirect('/login/')  # 重定向到登录页面
        else:
            if models.UserInfo.objects.filter(ticket=ticket).exists():  # 如果有匹配的ticket
                username = models.UserInfo.objects.filter(ticket=ticket)[0].user
                report_file = run.run(username)
                return render(request, report_file)

            else:  # 如果没有匹配的ticket
                return HttpResponseRedirect('/login/')
    else:
        print('截获get请求')
        # 获取令牌
        ticket = request.COOKIES.get('ticket')
        if not ticket:  # 如果cookie中没有ticket
            return HttpResponseRedirect('/login/')  # 重定向到登录页面
        else:
            if models.UserInfo.objects.filter(ticket=ticket).exists():  # 如果有匹配的ticket
                return render(request, 'runtest.html',{'name': models.UserInfo.objects.filter(ticket=ticket)[0].user})
            else:  # 如果没有匹配的ticket
                return HttpResponseRedirect('/login/')

def download_conf(request):
    file = open('conf/config.conf','rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="config.conf"'
    return response


def download_api(request):
    file = open('data/case_api.xlsx','rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="case_api.xlsx"'
    return response

def download_process(request):
    file = open('data/case_process.xlsx','rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="case_process.xlsx"'
    return response

