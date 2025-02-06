"""
https://www.kaoshibao.com/online/paper/detail/?paperid=16882563
"""

import requests
import time
import hashlib


def md5(s):
    m = hashlib.md5()
    m.update(s.encode('utf-8'))
    return m.hexdigest()


cookies = {
    'UM_distinctid': '194d99ce34581f-0d753cd1385de-4c657b58-1fa400-194d99ce3468a8',
    'Hm_lvt_975400bd703f587eef8de1efe396089d': '1738817725',
    'HMACCOUNT': '6F7DCF1B0993F072',
    'uu': 'd74796f7-8930-4420-b38a-b8a1ff4aa136',
    'CNZZDATA1278923901': '327821336-1738817725-https%253A%252F%252Fwww.baidu.com%252F%7C1738817809',
    'Hm_lpvt_975400bd703f587eef8de1efe396089d': '1738817809',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'CLIENT-IDENTIFIER': 'd74796f7-8930-4420-b38a-b8a1ff4aa136',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'UM_distinctid=194d99ce34581f-0d753cd1385de-4c657b58-1fa400-194d99ce3468a8; Hm_lvt_975400bd703f587eef8de1efe396089d=1738817725; HMACCOUNT=6F7DCF1B0993F072; uu=d74796f7-8930-4420-b38a-b8a1ff4aa136; CNZZDATA1278923901=327821336-1738817725-https%253A%252F%252Fwww.baidu.com%252F%7C1738817809; Hm_lpvt_975400bd703f587eef8de1efe396089d=1738817809',
    'Origin': 'https://www.kaoshibao.com',
    'Referer': 'https://www.kaoshibao.com/online/paper/detail/?paperid=16882563',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sign': 'df4ec76cee7a8e7d0e1294239ad39b6d',
    'TimeStamp': '1738823045244',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
    'platform': 'web',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'paperid': '16882563',
    'type': 'all',
    'size': 10,
    'page': 1,
}

o = "12b6bb84e093532fb72b4d65fec3f00b"  # 固定值
c = "d74796f7-8930-4420-b38a-b8a1ff4aa136"  # Cookie中的uuid
r = "/questions/lists"  # url的一部分
n = str(int(time.time() * 1000))

headers['TimeStamp'] = n
headers['Sign'] = md5(o + c + r + n + o)

response = requests.post('https://www.kaoshibao.com/api/questions/lists', cookies=cookies, headers=headers,
                         json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
# data = '{"paperid":"16882563","type":"all","size":10,"page":1}'
# response = requests.post('https://www.kaoshibao.com/api/questions/lists', cookies=cookies, headers=headers, data=data)

print(response.json())
