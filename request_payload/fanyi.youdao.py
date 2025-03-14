# https://fanyi.youdao.com/#/TextTranslate

import execjs
import requests

word = input("请输入要翻译的单词：")

# 先获取key, key不对的话翻译结果会错乱
cookies = {
    # 'JSESSIONID': 'abc5pgvVs9r3vdz7bdHuz',
    'OUTFOX_SEARCH_USER_ID': '1624354022@2409:8924:4cbe:6e1e:4c62:a573:9d8b:df1b',
    # 'OUTFOX_SEARCH_USER_ID_NCOO': '2077443144.8032303',
    # '_uetsid': '12d9f840009811f0a78113f1038b9aaa',
    # '_uetvid': '12da0aa0009811f09c212505ee1e0223',
    # 'DICT_DOCTRANS_SESSION_ID': 'N2U4MDczZWEtZTg3Yy00NzFjLTkxOTQtNTFjMDRmMWU0MjY2',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'JSESSIONID=abc5pgvVs9r3vdz7bdHuz; OUTFOX_SEARCH_USER_ID=1624354022@2409:8924:4cbe:6e1e:4c62:a573:9d8b:df1b; OUTFOX_SEARCH_USER_ID_NCOO=2077443144.8032303; _uetsid=12d9f840009811f0a78113f1038b9aaa; _uetvid=12da0aa0009811f09c212505ee1e0223; DICT_DOCTRANS_SESSION_ID=N2U4MDczZWEtZTg3Yy00NzFjLTkxOTQtNTFjMDRmMWU0MjY2',
}

response = requests.get(
    'https://dict.youdao.com/webtranslate/key?keyid=webfanyi-key-getter&sign=64f4ca9d718a931022461f5534d288a7&client=fanyideskweb&product=webfanyi&appVersion=1.0.0&vendor=web&pointParam=client,mysticTime,product&mysticTime=1741931370484&keyfrom=fanyi.web&mid=1&screen=1&model=1&network=wifi&abtest=0&yduuid=abcdefg',
    cookies=cookies,
    headers=headers,
)

# 这个key有时效性吗?
key = response.json()['data']['secretKey']

cookies = {
    # 'JSESSIONID': 'abc5pgvVs9r3vdz7bdHuz',
    'OUTFOX_SEARCH_USER_ID': '1624354022@2409:8924:4cbe:6e1e:4c62:a573:9d8b:df1b',
    # 'OUTFOX_SEARCH_USER_ID_NCOO': '2077443144.8032303',
    # '_uetsid': '12d9f840009811f0a78113f1038b9aaa',
    # '_uetvid': '12da0aa0009811f09c212505ee1e0223',
    # 'DICT_DOCTRANS_SESSION_ID': 'N2U4MDczZWEtZTg3Yy00NzFjLTkxOTQtNTFjMDRmMWU0MjY2',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'JSESSIONID=abckWzgSNk692fxiW7Xkz; OUTFOX_SEARCH_USER_ID_NCOO=1879393198.1356268; OUTFOX_SEARCH_USER_ID=-340494695@112.87.207.61; _uetsid=83f54070e52311efb5e0f56e4406b0ee; _uetvid=f7ec2d60d47811efb06675be584fef08; DICT_DOCTRANS_SESSION_ID=YWM0YWNjYjItNmJlMS00MDRkLWFlOGUtMGVkOWY0MDYxMjMy',
    'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'i': word,
    'from': 'auto',
    'to': '',
    'useTerm': 'false',
    'dictResult': 'true',
    'keyid': 'webfanyi',
    'sign': 'b95245d5b1fddeba5937666d596e5efb',
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': '1738912668484',
    'keyfrom': 'fanyi.web',
    'mid': '1',
    'screen': '1',
    'model': '1',
    'network': 'wifi',
    'abtest': '0',
    'yduuid': 'abcdefg',
}

with open('fanyi.youdao.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
ctx = execjs.compile(js_code)

params = ctx.call('getParams', key)

data['sign'] = params['sign']
data['mysticTime'] = params['mysticTime']

response = requests.post('https://dict.youdao.com/webtranslate', cookies=cookies, headers=headers, data=data)
encrypted_data = response.text

# 解密翻译结果
decoded_data = ctx.call('decode', encrypted_data)

print(decoded_data)
