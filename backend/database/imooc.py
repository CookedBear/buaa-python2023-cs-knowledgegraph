import requests
from requests import RequestException

from database import exception


def imooc_search(keyword):
    url = f'https://www.imooc.com/search/course?words={keyword}&source=&easy_type=&skill=&page=1'
    imooc = []
    try:
        html = requests.get(url).json()
        content_list = html['data']['hits']
        for data in content_list:
            courseName = data['_source']['title']
            difficulty = data['_source']['easy_type_name']
            numbers = data['_source']['numbers'] if 'numbers' in data['_source'] else data['_source']['collects']
            imgUrl = 'https:' + data['_source']['pic']
            courseUrl = data['_source']['target_url']
            print(courseName, difficulty, numbers, courseUrl)
            imooc.append({'name': courseName,
                          'difficulty': difficulty,
                          'plays': numbers,
                          'img': imgUrl,
                          'url': courseUrl})
    except RequestException as e:
        exception.do_exception("imooc ", keyword)

    return imooc
