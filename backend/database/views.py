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
from database.models import NodeInfo, User, Link, Favourite
from database import cnmooc, cmooc, xuetangx, icourse163, icourses, imooc, bilibili, study163


# Create your views here.
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
                        user=request.GET.get('username'), favourite=0)
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
        baseNode = NodeInfo(knowledgeName="计算机", relation=0, user=name, favourite=1)
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


@require_http_methods(['POST'])
def change_nodename(request):
    response = {}
    try:
        user = request.POST['username']
        oldname = request.POST['oldname']
        node = NodeInfo.objects.get(user=user, knowledgeName=oldname)
        node.knowledgeName = request.POST['newname']
        node.relation = request.POST['level']
        node.save()
        response['error'] = 0
        response['result'] = "Success"
    except Exception as e:
        response['error'] = 2
        response['result'] = "Other Error."

    return JsonResponse(response)


@require_http_methods(['POST'])
def change_favourite(request):
    response = {}
    try:
        user = request.POST['username']
        name = request.POST['nodename']
        node = NodeInfo.objects.get(user=user, knowledgeName=name)
        node.favourite = request.POST['favourite']
        node.save()
        response['error'] = 0
        response['result'] = "Success"
    except Exception as e:
        response['error'] = 2
        response['result'] = "Other Error."

    return JsonResponse(response)


@require_http_methods(['GET'])
def get_favourite(request):
    user = request.GET['username']
    response = {
        'nodes': json.loads(serializers.serialize("json", NodeInfo.objects.filter(user=user))), }
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
        'cnmooc': cnmooc.cnmooc_search(keyword),
        'cmooc': cmooc.cmooc_search(keyword),
        'xuetangx': xuetangx.xuetangx_search(keyword),
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


@require_http_methods(['GET'])
def favourite_graph(request):
    response = {}
    try:
        user = request.GET['username']
        filename = request.GET['graphname']
        if not os.path.exists("upload\\" + user):
            os.makedirs("upload\\" + user)

        graphs = Favourite.objects.filter(username=user, favourite=filename)
        if graphs:
            response['add_result'] = '已存在同名收藏'
            response['add_error'] = 1
            return JsonResponse(response)
        file = open("upload\\" + user + '\\' + filename + '.json', 'w')
        nodes = NodeInfo.objects.filter(user=user)
        graph = json.dumps({
            "nodes": json.loads(serializers.serialize("json", nodes)),
            "links": json.loads(serializers.serialize("json", Link.objects.filter(user=user)))})
        graph.replace("\'", "\"")
        file.write(graph)
        file.close()
        favourite = Favourite(favourite=filename, username=user, nodecount=nodes.count())
        favourite.save()

        response['add_error'] = 0
        response['add_result'] = 'favourite success'
    except Exception as e:
        response['add_error'] = 2
        response['add_result'] = 'Other Error.'
    return JsonResponse(response)


@require_http_methods(['GET'])
def delete_favourite_graph(request):
    response = {}
    try:
        user = request.GET['username']
        graph = request.GET['graphname']
        os.remove("upload\\" + user + '\\' + graph + '.json')
        Favourite.objects.filter(favourite=graph, username=user).delete()
        response['msg'] = ''
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = 'Other Error.'
        response['error_num'] = 2
    return JsonResponse(response)


@require_http_methods(['GET'])
def get_favourite_list(request):
    response = {}
    try:
        user = request.GET['username']
        response = {'graphs': json.loads(serializers.serialize("json", Favourite.objects.filter(username=user))),
                    'error_num': 0}
    except Exception as e:
        response['error_num'] = 2
    return JsonResponse(response)


@require_http_methods(['GET'])
def load_favourite(request):
    user = request.GET['username']
    favourite = request.GET['favourite']
    line = ''
    with open("upload\\" + user + '\\' + favourite + '.json', 'r') as file:
        line = file.readline()

    dicts = json.loads(line)
    Link.objects.filter(user=user).delete()
    NodeInfo.objects.filter(user=user).delete()
    for link in dicts['links']:
        linker = Link(source=link['fields']['source'], target=link['fields']['target'], name=link['fields']['name'],
                      user=link['fields']['user'])
        linker.save()
    for node in dicts['nodes']:
        noder = NodeInfo(knowledgeName=node['fields']['knowledgeName'], relation=node['fields']['relation'],
                         user=node['fields']['user'], favourite=node['fields']['favourite'])
        noder.save()
    message = {'code': 200, 'error_num': 0}
    return JsonResponse(message)


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
                             user=node['fields']['user'], favourite=node['fields']['favourite'])
            noder.save()

        if not os.path.exists(head_path):
            os.makedirs(head_path)
        file_suffix = file.name.split(".")[1]

        file_path = head_path + "\\{}".format(name + "." + file_suffix)
        file_path = file_path.replace(" ", "")
        with open(file_path, 'wb') as f:
            lines = file.readlines()
            for line in lines:
                f.write(line)

        message = {'code': 200, 'fileurl': file_path}
        return JsonResponse(message)


@require_http_methods(['GET'])
def init_graph(request):
    response = {}
    try:
        username = request.GET['username']
        Link.objects.filter(user=username).delete()
        NodeInfo.objects.filter(user=username).delete()
        initNode = NodeInfo(knowledgeName="计算机", relation=0, user=username, favourite=1)
        initNode.save()
        response['code'] = 0
        response['msg'] = 'Success'
    except Exception as e:
        response['code'] = 2
        response['msg'] = 'Other Error.'
    return JsonResponse(response)
