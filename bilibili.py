from database import exception
import requests
from requests import RequestException
from pypinyin import pinyin, Style

cookies = {
    'buvid3': 'CDA2F1DD-2DE9-4775-93BD-38D866B37261167611infoc'
}


def bilibili_search(keyword):
    params = {
        'keyword': keyword
    }
    url = 'https://api.bilibili.com/x/web-interface/search/all/v2'
    bilibili_default = []
    try:
        response = requests.get(url, params=params, cookies=cookies)
        html = response.json()
        content_list = html['data']['result'][11]['data']
        for data in content_list:
            courseName = str(str(data['title']).replace("<em class=\"keyword\">", "")).replace("</em>", "")
            play = int(data['play'])
            duration = data['duration']
            author = data['author']
            imgUrl = 'http:' + data['pic']
            courseUrl = data['arcurl']
            # print(courseName, play, duration, author, courseUrl)
            bilibili_default.append({'name': courseName,
                                     'author': author,
                                     'length': duration,
                                     'plays': play,
                                     'img': imgUrl,
                                     'url': courseUrl})

    except RequestException as e:
        exception.do_exception("bilibili", keyword)
    bilibili = {
        'default': bilibili_default,
        'name': sorted(bilibili_default, key=lambda x: [pinyin(i, style=Style.TONE3) for i in x['name']]),
        'plays': sorted(bilibili_default, key=lambda x: x['plays'], reverse=True),
    }
    return bilibili


if __name__ == '__main__':
    dic = bilibili_search('计算机科学与技术')
    # Sort the results based on 'play' count in descending order
    for key in dic.keys():
        print(key + ':')
        for data in dic[key]:
            print(data)
