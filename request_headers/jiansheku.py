# 网页: https://www.jiansheku.com/search/enterprise/
# API(翻页获得): https://capi.jiansheku.com/nationzj/enterprice/page
# 需要逆向的是请求头中的sign参数

import time

import execjs
import requests

page = input('请输入页码：')

json_data = {
    'eid': '',
    'achievementQueryType': 'and',
    'achievementQueryDto': [],
    'personnelQueryDto': {
        'queryType': 'and',
    },
    'aptitudeQueryDto': {
        'queryType': 'and',
        'nameStr': '',
        'aptitudeQueryType': 'and',
        'businessScopeQueryType': 'or',
        'filePlaceType': '1',
        'aptitudeDtoList': [
            {
                'codeStr': '',
                'queryType': 'and',
                'aptitudeType': 'qualification',
            },
        ],
        'aptitudeSource': 'new',
    },
    'page': {
        'page': page,
        'limit': 20,
        'field': '',
        'order': '',
    },
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://www.jiansheku.com',
    'Referer': 'https://www.jiansheku.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'deviceType': 'PC',
    'page': 'search-enterprise',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sign': '7e53f1a2da1d10536b462fce4509eb3c',
    'timestamp': '1741854747559',
}

timestamp = int(round(time.time() * 1000))

with open('jiansheku.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
    ctx = execjs.compile(js_code)

headers['sign'] = ctx.call('getSign', json_data, timestamp)
headers['timestamp'] = str(timestamp)

response = requests.post('https://capi.jiansheku.com/nationzj/enterprice/page', headers=headers, json=json_data)

print(response.json())
