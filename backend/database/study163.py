import requests


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
                print(course[1])
                print(course[1]["productName"], course[1]["provider"],
                      course[1]["learnerCount"], course[1]["lectorName"],
                      course[1]["bigImgUrl"])
                study163.append({
                    'name': course[1]["productName"],
                    'teacherName': course[1]["lectorName"],
                    'schoolName': course[1]["provider"],
                    'plays': course[1]["learnerCount"],
                    'img': course[1]["bigImgUrl"]
                })
    except:
        print("出错了")

    return study163
