import requests
from bs4 import BeautifulSoup
from requests import RequestException

from exception import do_exception


def icourses_search(keyword):
    cookies = {
        '_uab_collina': '168976447742522645437531'
    }
    data = {
        'kw': keyword
    }
    url = 'https://www.icourses.cn/web/sword/portalsearch/homeSearch'
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
            print(courseName, courseType, schoolName, teacherName, courseUrl)
    except RequestException as e:
        do_exception("icourses", keyword)
