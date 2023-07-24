import requests
from database import exception


def study163_search(keyword):
    url = "https://study.163.com/p/search/studycourse.json"

    payload = {
        "activityId": 0,
        "keyword": keyword,
        "orderType": 5,
        "pageIndex": 1,
        "pageSize": 50,
        "priceType": -1,
        "qualityType": 0,
        "relativeOffset": 0,
        "searchTimeType": -1,
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "origin": "https://study.163.com",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    }
    study163 = []
    try:
        response = requests.post(url, json=payload, headers=headers)
        content = response.json()
        if content and content["code"] == 0:
            course_list = content["result"]["list"]
            for course in enumerate(course_list):
                productName = course[1]["productName"]
                productId = course[1]['productId']
                courseId = course[1]['courseId']
                provider = course[1]["provider"]
                learnerCount = course[1]["learnerCount"]
                imgUrl = course[1]["bigImgUrl"]
                if learnerCount is None:
                    productUrl = f'https://mooc.study.163.com/course/{courseId}#/info'
                    print(productName, provider, productUrl)
                else:
                    productUrl = f'https://study.163.com/course/introduction/{productId}.htm'
                    # print('项目课程：', productName, provider, learnerCount, productUrl)
                study163.append({
                    'name': productName,
                    'teacherName': provider,
                    'plays': learnerCount,
                    'img': imgUrl,
                    'url': productUrl
                })
    except:
        exception.do_exception("study163", keyword)
    return study163
