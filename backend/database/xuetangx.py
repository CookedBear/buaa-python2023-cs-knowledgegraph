import requests
from pypinyin import pinyin, Style

from database import exception


def xuetangx_search(keyword):
    cookies = {
        '_abfpc': '20ff75f890f7fe8c50ca9bc1947023bee6bf9a1c_2.0',
        'cna': '2b444e4c19ab13db0ab9159d9484588c',
        'provider': 'xuetang',
        'django_language': 'zh',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221899c5fbf7210c1-087514282c632b8-26031c51-3686400-1899c5fbf73138a%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.bing.com%2F%22%7D%2C%22%24device_id%22%3A%221899c5fbf7210c1-087514282c632b8-26031c51-3686400-1899c5fbf73138a%22%7D',
        'point': '{%22point_active%22:true%2C%22platform_task_active%22:true%2C%22learn_task_active%22:true}',
        'PPA_CI': '676ca6db68aaf3a66c115bae9218490a',
        'JG_016f5b1907c3bc045f8f48de1_PV': '1690561121504|1690561162197',
    }
    headers = {
        'authority': 'www.xuetangx.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh',
        'app-name': 'xtzx',
        'content-type': 'application/json',
        # 'cookie': '_abfpc=20ff75f890f7fe8c50ca9bc1947023bee6bf9a1c_2.0; cna=2b444e4c19ab13db0ab9159d9484588c; provider=xuetang; django_language=zh; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221899c5fbf7210c1-087514282c632b8-26031c51-3686400-1899c5fbf73138a%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.bing.com%2F%22%7D%2C%22%24device_id%22%3A%221899c5fbf7210c1-087514282c632b8-26031c51-3686400-1899c5fbf73138a%22%7D; point={%22point_active%22:true%2C%22platform_task_active%22:true%2C%22learn_task_active%22:true}; PPA_CI=676ca6db68aaf3a66c115bae9218490a; JG_016f5b1907c3bc045f8f48de1_PV=1690561121504|1690561162197',
        'django-language': 'zh',
        'origin': 'https://www.xuetangx.com',
        'referer': 'https://www.xuetangx.com/search?query=%E8%AE%A1%E7%AE%97%E6%9C%BA&page=1&ss=manual_search&channel=i.area.manual_search',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'terminal-type': 'web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'x-client': 'web',
        'xtbz': 'xt',
    }
    params = {
        'page': '1',
    }
    data = f'{{"query":"{keyword}","chief_org":[],"classify":[],"selling_type":[],"status":[],"appid":10000}}'.encode()
    xuetangx_default = []
    try:
        response = requests.post(
            'https://www.xuetangx.com/api/v1/lms/get_product_list/',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        html = response.json()
        content_list = html['data']['product_list']
        for data in content_list:
            if len(data['teacher']) == 0:
                continue
            courseName = data['name']
            teacherName = data['teacher'][0]['name']
            schoolName = data['teacher'][0]['org_name']
            count = data['count']
            imgUrl = data['cover']
            courseUrl = 'https://www.xuetangx.com/course/' + data['sign'] + '/' + str(data['course_id'])
            # print(courseName, schoolName, teacherName, courseUrl)
            xuetangx_default.append({'name': courseName,
                                     'author': teacherName,
                                     'school': schoolName,
                                     'plays': count,
                                     'img': imgUrl,
                                     'url': courseUrl})
    except:
        exception.do_exception("xuetangx", keyword)

    xuetangx = {
        'default': xuetangx_default,
        'name': sorted(xuetangx_default, key=lambda x: [pinyin(i, style=Style.TONE3) for i in x['name']]),
        'plays': sorted(xuetangx_default, key=lambda x: x['plays'], reverse=True),
    }
    return xuetangx


if __name__ == '__main__':
    dic = xuetangx_search('计算机')
    # Sort the results based on 'play' count in descending order
    for key in dic.keys():
        print(key + ':')
        for data in dic[key]:
            print(data)
