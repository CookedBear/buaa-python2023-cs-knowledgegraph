import requests
from bs4 import BeautifulSoup
from pypinyin import pinyin, Style
from requests import RequestException

from database import exception


def icourses_search(keyword):
    cookies = {
        '_uab_collina': '168976447742522645437531'
    }
    data = {
        'kw': keyword
    }
    url = 'https://www.icourses.cn/web/sword/portalsearch/homeSearch'
    icourses_default = []
    try:
        response = requests.post(url, data=data, cookies=cookies)
        soup = BeautifulSoup(response.text, 'html.parser')
        content_list = soup.find_all(class_='icourse-item-modulebox')
        for data in content_list:
            courseName = data.find(class_='icourse-desc-title').text
            courseTypeElement = data.findNext(class_='icourse-desc-school')
            teacherName, schoolName = courseTypeElement.findNext(class_='icourse-desc-school').text.split(' | ')
            courseType = courseTypeElement.text
            imgUrl = data.find('img')['src']
            courseUrl = data.find(class_='icourse-desc-title')['href']
            if courseUrl.startswith('//'):
                # icourses的文件没有前缀http:，需要加上
                courseUrl = 'http:' + courseUrl
            # print(courseName, courseType, schoolName, teacherName, courseUrl)
            icourses_default.append({'name': courseName,
                                     'author': teacherName,
                                     'school': schoolName,
                                     'type': courseType,
                                     'img': imgUrl,
                                     'u rl': courseUrl})
    except RequestException as e:
        exception.do_exception("icourses", keyword)
    icourses = {
        'default': icourses_default,
        'name': sorted(icourses_default, key=lambda x: [pinyin(i, style=Style.TONE3) for i in x['name']]),
        'school': sorted(icourses_default, key=lambda x: [pinyin(i, style=Style.TONE3) for i in x['school']]),
    }
    return icourses


if __name__ == '__main__':
    dic = icourses_search('计算机')
    # Sort the results based on 'play' count in descending order
    for key in dic.keys():
        print(key + ':')
        for data in dic[key]:
            print(data)
