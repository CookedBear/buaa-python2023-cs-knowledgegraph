import requests

cookies = {
    'buvid3': 'CDA2F1DD-2DE9-4775-93BD-38D866B37261167611infoc'
}


def bilibili_search(string):
    params = {
        'keyword': string
    }
    url = 'https://api.bilibili.com/x/web-interface/search/all/v2'
    response = requests.get(url, params=params, cookies=cookies)
    html = response.json()
    content_list = html['data']['result'][11]['data']
    for data in content_list:
        s = data['title']
        s1 = str(s).replace("<em class=\"keyword\">", "")
        s2 = str(s1).replace("</em>", "")
        print(s2, data['play'], data['duration'], data['author'], data['arcurl'])
    # print(response)
    # with open('result.json', 'w', encoding='gb18030') as file:
    #     json.dump(response, file)
    # print()
