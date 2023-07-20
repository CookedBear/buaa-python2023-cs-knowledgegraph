# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import json
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from database.models import NodeInfo
from database.models import User


# Create your views here.
# add_student接受一个get请求，往数据库里添加一条Student数据
@require_http_methods(["GET"])
def add_node(request):
    response = {}
    try:
        node = NodeInfo(knowledgeName=request.GET.get('knowledgeName'), relation=request.GET.get('relation'))
        node.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


# show_students返回所有的书籍列表（通过JsonResponse返回能被前端识别的json格式数据）
@require_http_methods(["GET"])
def show_nodes(request):
    response = {}
    try:
        nodes = NodeInfo.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", nodes))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["POST"])
def login_in(request):
    response = {}
    try:
        name = request.POST['username']
        key = request.POST["password"]
        user = User.objects.filter(username=name).first()
        if user.password != key:
            response['login_error'] = 1
            response['login_result'] = '密码错误'
            return JsonResponse(response)
        # user = User(username=name, password=key)
        # user.save()
        response['login_error'] = 0
        response['login_result'] = ''
    except Exception as e:   # 查人失败了
        response['login_error'] = 2
        response['login_result'] = '用户不存在'

    return JsonResponse(response)


@require_http_methods(["POST"])
def register(request):
    response = {}
    users = 0
    try:
        name = request.POST['username']
        key = request.POST["password"]
        users = User.objects.values('username')
        if {'username': name} in users:
            response['register_error'] = 1
            response['register_result'] = '用户已存在'
            return JsonResponse(response)
        user = User(username=name, password=key)
        user.save()
        response['register_error'] = 0
        response['register_result'] = ''
    except Exception as e:
        response['login_error'] = 2
        response['login_result'] = "Other Error."

    return JsonResponse(response)
