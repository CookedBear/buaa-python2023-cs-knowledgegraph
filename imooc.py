import requests
from pypinyin import pinyin, Style
from requests import RequestException

from database import exception


def imooc_search(keyword):
    url = f'https://www.imooc.com/search/course?words={keyword}&source=&easy_type=&skill=&page=1'
    imooc_default = []
    try:
        html = requests.get(url).json()
        content_list = html['data']['hits']
        for data in content_list:
            courseName = data['_source']['title']
            difficulty = data['_source']['easy_type_name']
            numbers = data['_source']['numbers'] if 'numbers' in data['_source'] else data['_source']['collects']
            if type(numbers) is str:
                numbers = int(numbers)
            imgUrl = 'https:' + data['_source']['pic']
            courseUrl = data['_source']['target_url']
            # print(courseName, difficulty, numbers, courseUrl)
            imooc_default.append({'name': courseName,
                                  'difficulty': difficulty,
                                  'plays': numbers,
                                  'img': imgUrl,
                                  'url': courseUrl})
    except RequestException as e:
        exception.do_exception("imooc ", keyword)
    imooc = {
        'default': imooc_default,
        'name': sorted(imooc_default, key=lambda x: [pinyin(i, style=Style.TONE3) for i in x['name']]),
        'plays': sorted(imooc_default, key=lambda x: x['plays'], reverse=True),
    }
    return imooc


if __name__ == '__main__':
    dic = imooc_search('计算机科学与技术')
    # Sort the results based on 'play' count in descending order
    for key in dic.keys():
        print(key + ':')
        for data in dic[key]:
            print(data)
