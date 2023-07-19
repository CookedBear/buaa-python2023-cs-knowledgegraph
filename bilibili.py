import requests
import time
import json
import jsonpath

headers = {'cookie': 'buvid3=CDA2F1DD-2DE9-4775-93BD-38D866B37261167611infoc;',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
           'referer': 'https://www.bilibili.com',
           'sec-fetch-dest': 'script',
           'sec-fetch-mode': 'no-cors',
           'sec-fetch-site': 'same-site',
           }


def get_parse(result):
    ans = jsonpath.jsonpath(result, '$.data.result[11]')
    s = ans[0]['data'][0]['title']
    s1 = str(s).replace("<em class=\"keyword\">", "")
    s2 = str(s1).replace("</em>", "")
    print(s2, ans[0]['data'][0]['play'], ans[0]['data'][0]['duration'], ans[0]['data'][0]['author'],
          ans[0]['data'][0]['arcurl'])


def bilibili_search(string):
    for i in range(1, 50):
        url = 'https://api.bilibili.com/x/web-interface/search/all/v2?keyword={}&page={}'.format(string, i)
        response = requests.get(url, headers=headers).json()
        get_parse(response)
        # print(response)
        # with open('result.json', 'w', encoding='gb18030') as file:
        #     json.dump(response, file)
        # print()

