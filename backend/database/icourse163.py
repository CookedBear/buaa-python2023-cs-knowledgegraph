import requests
from requests import RequestException

from database import exception


def icourse163_search(keyword):
    cookies = {
        'NTESSTUDYSI': 'd51a29034358496ca77d3f522cca3dc0'
    }
    data = {
        'mocCourseQueryVo': '{'
                            f'\"keyword\":\"{keyword}\",'
                            '\"pageIndex\":1,'
                            '\"highlight\":true,'
                            '\"orderBy\":0,'
                            '\"stats\":30,'
                            '\"pageSize\":20'
                            '}'
    }
    url = 'https://www.icourse163.org/web/j/mocSearchBean.searchCourse.rpc?csrfKey=d51a29034358496ca77d3f522cca3dc0'
    icourse163 = []
    try:
        response = requests.post(url, data=data, cookies=cookies)
        html = response.json()
        content_list = html['result']['list']
        if content_list is None:
            content_list = []
        for data in content_list:
            if data['type'] != 306:
                continue  # 过滤广告
            className = data['mocCourseCard']['mocCourseCardDto']['name']
            schoolName = data['highlightUniversity']
            schoolShortName = data['mocCourseCard']['mocCourseCardDto']['schoolPanel']['shortName']
            teacherName = data['highlightTeacherNames']
            enrollCount = data['mocCourseCard']['enrollCount']
            courseId = data['courseId']
            imgUrl = data['mocCourseCard']['mocCourseCardDto']['imgUrl']
            courseUrl = f'https://www.icourse163.org/course/{schoolShortName}-{courseId}'
            print(className, schoolName, teacherName, enrollCount, courseUrl)
            icourse163.append({'name': className,
                               'author': teacherName,
                               'school': schoolName,
                               'plays': enrollCount,
                               'img': imgUrl,
                               'url': courseUrl})
    except RequestException as e:
        exception.do_exception("icourse163", keyword)

    return icourse163
