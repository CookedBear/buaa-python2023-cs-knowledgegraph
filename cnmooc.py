import requests
from bs4 import BeautifulSoup
from pypinyin import pinyin, Style
from database import exception


def cnmooc_search(keyword):
    headers = {
        'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        'Referer': 'https://www.cnmooc.org/home/index.mooc',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': 'moocvk=318dbc142ac246c88a58212b12becd3f; cpstk=7797e129832146c1adb5051e82c4b7e2; Hm_lvt_ed399044071fc36c6b711fa9d81c2d1c=1689788346; PPA_CI=2ad519ece39b6ca505fdd890e636879c; JSESSIONID=6B5EE0D9B474961DE6A5E47413E9402A.tomcat-1; BEC=8a00e34a4073e76c4f8529c13c4cc82e; Hm_lpvt_ed399044071fc36c6b711fa9d81c2d1c=1690006275'
    }
    url = 'https://www.cnmooc.org/portal/ajaxCourseIndex.mooc'
    cnmooc_default = []
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
            cnmooc_default.append({
                'name': courseName,
                'author': teacherName,
                'school': schoolName,
                'plays': courseTime,
                'img': imgUrl,
                'url': courseUrl
            })
    except Exception as e:
        exception.do_exception("cnmooc", keyword)
    cnmooc = {
        'default': cnmooc_default,
        'name': sorted(cnmooc_default, key=lambda x: [pinyin(i, style=Style.TONE3) for i in x['name']]),
        'school': sorted(cnmooc_default, key=lambda x: [pinyin(i, style=Style.TONE3) for i in x['school']]),
    }
    return cnmooc


if __name__ == '__main__':
    dic = cnmooc_search('计算机')
    # Sort the results based on 'play' count in descending order
    for key in dic.keys():
        print(key + ':')
        for data in dic[key]:
            print(data)
