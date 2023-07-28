import requests

import requests
from bs4 import BeautifulSoup
from pypinyin import pinyin, Style
from requests import RequestException

from database import exception


def cmooc_search(keyword):
    cookies = {
        'PPA_CI': '5c48274ef3d7f8a7396b573ace42d8e1',
        'screen': '1125',
    }
    headers = {
        'authority': 'www.cmooc.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'PPA_CI=5c48274ef3d7f8a7396b573ace42d8e1; screen=1125',
        'referer': 'https://www.cmooc.com/',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }
    params = {
        's': '计算机',
        'cat': '5',
    }

    cmooc_default = []
    try:
        response = requests.get('https://www.cmooc.com/', params=params, cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        content_list = soup.find_all(class_='course-list')
        for data in content_list:
            courseName = data.find(class_='courselist-title').contents[1].text
            schoolName = data.find(class_='course-nm course-sch').text
            courseDifficult = data.find(class_='course-nm course-tip').text
            plays = int(''.join(filter(lambda x: x.isdigit(), data.find(class_='course-nm course-tip-last').text)))
            imgUrl = data.find('img')['src']
            courseUrl = data.find(class_='courselist-title').contents[1].attrs['href']
            # print(courseName, courseType, schoolName, teacherName, courseUrl)
            cmooc_default.append({'name': courseName,
                                  'school': schoolName,
                                  'difficulty': courseDifficult,
                                  'plays': plays,
                                  'img': imgUrl,
                                  'url': courseUrl})
    except RequestException as e:
        exception.do_exception("cmooc", keyword)
    cmooc = {
        'default': cmooc_default,
        'name': sorted(cmooc_default, key=lambda x: [pinyin(i, style=Style.TONE3) for i in x['name']]),
        'school': sorted(cmooc_default, key=lambda x: x['plays'], reverse=True),
    }
    return cmooc


if __name__ == '__main__':
    dic = cmooc_search('计算机')
    # Sort the results based on 'play' count in descending order
    for key in dic.keys():
        print(key + ':')
        for data in dic[key]:
            print(data)
