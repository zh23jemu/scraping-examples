from hashlib import md5

import requests


def u(t):
    o = '9SASji5OWnG41iRKiSvTJHlXHmRySRp1'
    result = (t + '&' + o).lower()

    return md5(result.encode()).hexdigest()


url = "https://uwf7de983aad7a717eb.youzy.cn/youzy.dms.basiclib.api.college.query"

# 通过引号将数据封装成json格式
payload = '{"keyword":"","provinceNames":[],"natureTypes":[],"eduLevel":"","categories":[],"features":[],"pageIndex":2,"pageSize":20,"sort":11}'
headers = {
    "u-sign": u(payload),
    "Content-Type": "application/json"  # Content-Type不能少
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())
