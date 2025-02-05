"""
https://wx.qmpsee.com/articleDetail?id=4fa969798f4e5e6a9c5e5a6067385d9d
https://research.qmpsee.com/industry-insight
"""
import execjs
import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://wx.qmpsee.com',
    'Platform': 'web',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Source': 'see',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'page': '1',
    'num': '20',
    'ca_uuid': '4fa969798f4e5e6a9c5e5a6067385d9d',
}

with requests.post('https://wyiosapi.qmpsee.com/Web/getCaDetail', headers=headers, data=data) as r:
    encrypt_data = r.json()['encrypt_data']

with open('qmpsee.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)

print(ctx.call('Mc', encrypt_data))

# print(encrypt_data)
