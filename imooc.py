# coding:utf8
import jsonpath
import requests
import random
import json
from ua_info import ua_list


# 获取随机headers
def get_headers():
    headers = {'User-Agent': random.choice(ua_list)}
    return headers


def get_parse(result):
    ans = jsonpath.jsonpath(result, '$.data.hits')
    for dic in ans[0]:
        print(dic["_source"]["title"], dic["_source"]["numbers"], dic["_source"]["target_url"])
    return ans


def imooc_search(string):
    url = 'https://www.imooc.com/search/course?words={}&source=&easy_type=&skill=&page=1'.format(string)
    headers = get_headers()
    html = requests.get(url=url, headers=headers).json()
    html = get_parse(html)
    # with open('result.json', 'w', encoding='gb18030') as file:
    #     json.dump(html, file)
