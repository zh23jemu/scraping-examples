import execjs
import requests

word = input("请输入要翻译的单词：")
# 1. 获取翻译结果

cookies = {
    'JSESSIONID': 'abckWzgSNk692fxiW7Xkz',
    'OUTFOX_SEARCH_USER_ID_NCOO': '1879393198.1356268',
    'OUTFOX_SEARCH_USER_ID': '-340494695@112.87.207.61',
    '_uetsid': '83f54070e52311efb5e0f56e4406b0ee',
    '_uetvid': 'f7ec2d60d47811efb06675be584fef08',
    'DICT_DOCTRANS_SESSION_ID': 'YWM0YWNjYjItNmJlMS00MDRkLWFlOGUtMGVkOWY0MDYxMjMy',
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

params = ctx.call('getParams')

data['sign'] = params['sign']
data['mysticTime'] = params['mysticTime']

response = requests.post('https://dict.youdao.com/webtranslate', cookies=cookies, headers=headers, data=data)

encrypted_data = response.text

# 2. 解密翻译结果
decoded_data = ctx.call('decode', encrypted_data)

print(decoded_data)
