# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import json
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.db.models import Q
from django.views.decorators.http import require_http_methods
from database.models import NodeInfo
from database.models import User
from database.models import Link


# Create your views here.
# add_student接受一个get请求，往数据库里添加一条Student数据
@require_http_methods(["GET"])
def add_node(request):
    response = {}
    try:
        nodes = NodeInfo.objects.filter(knowledgeName=request.GET.get('knowledgeName'))
        if nodes:
            response['msg'] = '节点已存在'
            response['error_num'] = 1
            return JsonResponse(response)
        node = NodeInfo(knowledgeName=request.GET.get('knowledgeName'), relation=request.GET.get('relation'))
        node.save()
        response['msg'] = 'add node success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 2

    return JsonResponse(response)


@require_http_methods(["POST"])
def del_node(request):
    response = {}
    try:
        node = request.POST['del_node']
        NodeInfo.objects.filter(knowledgeName=node).delete()
        Link.objects.filter(source=node).delete()
        Link.objects.filter(target=node).delete()
        response['msg'] = ''
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 2
    return JsonResponse(response)


@require_http_methods(["POST"])
def del_line(request):
    response = {}
    try:
        Link.objects.filter(source=request.POST['source'], target=request.POST['target']).delete()
        Link.objects.filter(source=request.POST['target'], target=request.POST['source']).delete()
        response['msg'] = ''
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 2
    return JsonResponse(response)


# show_students返回所有的书籍列表（通过JsonResponse返回能被前端识别的json格式数据）
@require_http_methods(["GET"])
def show_nodes(request):
    response = {}
    try:
        nodes = NodeInfo.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", nodes))
        response['msg'] = 'show node success'
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
        response['login_result'] = 'login in success'
    except Exception as e:  # 查人失败了
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
        response['register_result'] = 'register success'
    except Exception as e:
        response['login_error'] = 2
        response['login_result'] = "Other Error."

    return JsonResponse(response)


@require_http_methods(['GET'])
def add_relation(request):
    response = {}
    try:
        node1 = request.GET['source']
        node2 = request.GET['target']
        node1, node2 = [min(node1, node2), max(node1, node2)]
        links = Link.objects.filter(source=node1, target=node2)
        if links:
            response['add_error'] = 1
            response['add_result'] = '关系已存在'
            return JsonResponse(response)

        link = Link(source=node1, target=node2, name=request.GET['name'])
        link.save()
        response['add_error'] = 0
        response['add_result'] = 'add relation success'
    except Exception as e:
        response['add_error'] = 2
        response['add_result'] = 'Other Error.'
    return JsonResponse(response)


@require_http_methods(['GET'])
def read_graph(request):
    response = {
        'nodes': json.loads(serializers.serialize("json", NodeInfo.objects.all())),
        'links': json.loads(serializers.serialize("json", Link.objects.all()))}
    return JsonResponse(response)
