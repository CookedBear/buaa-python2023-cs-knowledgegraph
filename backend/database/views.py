# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.shortcuts import render
import json
from django.http import JsonResponse, FileResponse
from django.core import serializers
from django.shortcuts import render
from django.db.models import Q
from django.views.decorators.http import require_http_methods
from database.models import NodeInfo
from database.models import User
from database.models import Link
from database import cnmooc
from database import icourse163
from database import icourses
from database import imooc
from database import bilibili
from database import study163


# Create your views here.
# add_student接受一个get请求，往数据库里添加一条Student数据
@require_http_methods(["GET"])
def add_node(request):
    response = {}
    try:
        nodes = NodeInfo.objects.filter(knowledgeName=request.GET.get('knowledgeName'),
                                        user=request.GET.get('username'))
        if nodes:
            response['msg'] = '节点已存在'
            response['error_num'] = 1
            return JsonResponse(response)
        node = NodeInfo(knowledgeName=request.GET.get('knowledgeName'), relation=request.GET.get('relation'),
                        user=request.GET.get('username'))
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
        user = request.POST['username']
        NodeInfo.objects.filter(knowledgeName=node, user=user).delete()
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
        Link.objects.filter(source=request.POST['source'], target=request.POST['target'],
                            user=request.POST['username']).delete()
        Link.objects.filter(source=request.POST['target'], target=request.POST['source'],
                            user=request.POST['username']).delete()
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
        baseNode = NodeInfo(knowledgeName="Root", relation=0, user=name)
        baseNode.save()
        response['register_error'] = 0
        response['register_result'] = 'register success'
    except Exception as e:
        response['login_error'] = 2
        response['login_result'] = "Other Error."

    return JsonResponse(response)


@require_http_methods(['POST'])
def change_password(request):
    response = {}
    try:
        user = request.POST['username']
        password = request.POST['newPassword']
        USER = User.objects.get(username=user)
        USER.password = password
        USER.save()
        response['error'] = 0
        response['result'] = "Success"
    except Exception as e:
        response['error'] = 2
        response['result'] = "Other Error."

    return JsonResponse(response)


@require_http_methods(['GET'])
def add_relation(request):
    response = {}
    try:
        node1 = request.GET['source']
        node2 = request.GET['target']
        user = request.GET['username']
        node1, node2 = [min(node1, node2), max(node1, node2)]
        links = Link.objects.filter(source=node1, target=node2, user=user)
        if links:
            response['add_error'] = 1
            response['add_result'] = '关系已存在'
            return JsonResponse(response)

        link = Link(source=node1, target=node2, name=request.GET['name'], user=user)
        link.save()
        response['add_error'] = 0
        response['add_result'] = 'add relation success'
    except Exception as e:
        response['add_error'] = 2
        response['add_result'] = 'Other Error.'
    return JsonResponse(response)


@require_http_methods(['GET'])
def read_graph(request):
    user = request.GET['username']
    response = {
        'nodes': json.loads(serializers.serialize("json", NodeInfo.objects.filter(user=user))),
        'links': json.loads(serializers.serialize("json", Link.objects.filter(user=user)))}
    return JsonResponse(response)


@require_http_methods(['GET'])
def get_creep_content(request):
    keyword = request.GET['knowledge']
    response = {
        'bilibili': bilibili.bilibili_search(keyword),
        # 'cnmooc': cnmooc.cnmooc_search(keyword),
        'icourse163': icourse163.icourse163_search(keyword),
        'icourses': icourses.icourses_search(keyword),
        'imooc': imooc.imooc_search(keyword),
        'study163': study163.study163_search(keyword),
        'cnmooc': cnmooc.cnmooc_search(keyword)
    }
    return JsonResponse(response)


@require_http_methods(['GET'])
def download_graph(request):
    user = request.GET['username']
    file = open("upload\\" + user + '.json', 'w')
    graph = json.dumps({
        "nodes": json.loads(serializers.serialize("json", NodeInfo.objects.filter(user=user))),
        "links": json.loads(serializers.serialize("json", Link.objects.filter(user=user)))})
    graph.replace("\'", "\"")
    print(graph)
    file.write(graph)
    file.close()
    response = FileResponse(open("upload\\" + user + '.json', 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    # name.split('.')[0] + '.docx'，
    name = user + '_graph.json'
    response['Content-Disposition'] = 'attachment;filename ="%s"' % (
        name.encode('utf-8').decode('ISO-8859-1'))
    return response


@require_http_methods(['POST'])
def upload_graph(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    name = request.POST['username']
    if request.method == 'POST':
        file = request.FILES.get('file', None)
        line = (file.readline().decode('gb2312'))

        dicts = json.loads(line)
        # 设置文件上传文件夹
        head_path = BASE_DIR + "\\upload\\json"
        # delete nodes & links
        Link.objects.filter(user=name).delete()
        NodeInfo.objects.filter(user=name).delete()
        # add new data
        for link in dicts['links']:
            print(link)
            linker = Link(source=link['fields']['source'], target=link['fields']['target'], name=link['fields']['name'],
                          user=link['fields']['user'])
            linker.save()
        for node in dicts['nodes']:
            noder = NodeInfo(knowledgeName=node['fields']['knowledgeName'], relation=node['fields']['relation'],
                             user=node['fields']['user'])
            noder.save()

        # 判断是否存在文件夹, 如果没有就创建文件路径
        if not os.path.exists(head_path):
            os.makedirs(head_path)
        file_suffix = file.name.split(".")[1]  # 获取文件后缀
        # 储存路径
        file_path = head_path + "\\{}".format(name + "." + file_suffix)
        file_path = file_path.replace(" ", "")
        # 上传文件
        with open(file_path, 'wb') as f:
            lines = file.readlines()
            for line in lines:
                f.write(line)

        message = {'code': 200, 'fileurl': file_path}
        # 返回图片路径

        return JsonResponse(message)
