import requests
from bs4 import BeautifulSoup

from exception import do_exception


def cnmooc_search(keyword):
    headers = {
        'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        'Referer': 'https://www.cnmooc.org/home/index.mooc',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': 'moocvk=318dbc142ac246c88a58212b12becd3f; cpstk=7797e129832146c1adb5051e82c4b7e2; Hm_lvt_ed399044071fc36c6b711fa9d81c2d1c=1689788346; PPA_CI=2ad519ece39b6ca505fdd890e636879c; JSESSIONID=6B5EE0D9B474961DE6A5E47413E9402A.tomcat-1; BEC=8a00e34a4073e76c4f8529c13c4cc82e; Hm_lpvt_ed399044071fc36c6b711fa9d81c2d1c=1690006275'
    }
    url = 'https://www.cnmooc.org/portal/ajaxCourseIndex.mooc'
    data = {
        'keyWord': {keyword},
        'openFlag': '0',
        'fromType': '',
        'learningMode': '0',
        'certType': '',
        'languageId': '',
        'categoryId': '',
        'menuType': 'course',
        'schoolId': '',
        'pageIndex': '1',
        'postoken': '7797e129832146c1adb5051e82c4b7e2'
    }
    try:
        response = requests.post(url, data=data, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        content_list = soup.find_all(class_='view-item')
        for data in content_list:
            courseName = ''.join(data.find(class_='link-default').contents[0].split())
            courseTime = data.find(class_='cview-time').text
            teacherName = data.find(class_='t-name').text
            schoolName = data.find(class_='t-school').text
            imgUrl = data.find(class_='view-img').find('img')['src']
            courseUrl = 'https://www.cnmooc.org/' + data.find(class_='view-img')['href']
            print(courseName, courseTime, schoolName, teacherName, courseUrl)
    except Exception as e:
        do_exception("cnmooc", keyword)
