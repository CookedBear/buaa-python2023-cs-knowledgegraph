from exception import do_exception
import requests
from requests import RequestException

cookies = {
    'buvid3': 'CDA2F1DD-2DE9-4775-93BD-38D866B37261167611infoc'
}


def bilibili_search(keyword):
    params = {
        'keyword': keyword
    }
    url = 'https://api.bilibili.com/x/web-interface/search/all/v2'
    try:
        response = requests.get(url, params=params, cookies=cookies)
        html = response.json()
        content_list = html['data']['result'][11]['data']
        for data in content_list:
            courseName = str(str(data['title']).replace("<em class=\"keyword\">", "")).replace("</em>", "")
            play = data['play']
            duration = data['duration']
            author = data['author']
            imgUrl = 'http:' + data['pic']
            courseUrl = data['arcurl']
            print(courseName, play, duration, author, courseUrl)
    except RequestException as e:
        do_exception("bilibili", keyword)

