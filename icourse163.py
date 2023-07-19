import requests


def icourse163_search(keyword):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'cookie': 'NTESSTUDYSI=d51a29034358496ca77d3f522cca3dc0;'
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
    response = requests.post(url, headers=headers, data=data)
    html = response.json()
    content_list = html['result']['list']
    for data in content_list:
        className = data['mocCourseCard']['mocCourseCardDto']['name']
        schoolName = data['highlightUniversity']
        schoolShortName = data['mocCourseCard']['mocCourseCardDto']['schoolPanel']['shortName']
        teacherName = data['highlightTeacherNames']
        enrollCount = data['mocCourseCard']['enrollCount']
        courseId = data['courseId']
        courseUrl = f'https://www.icourse163.org/course/{schoolShortName}-{courseId}'
        print(className, schoolName, teacherName, enrollCount, courseUrl)
