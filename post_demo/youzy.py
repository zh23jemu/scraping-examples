import requests

url = "https://uwf7de983aad7a717eb.youzy.cn/youzy.dms.basiclib.api.college.query"

# 通过引号将数据封装成json格式
payload = '{"keyword":"","provinceNames":[],"natureTypes":[],"eduLevel":"","categories":[],"features":[],"pageIndex":1,"pageSize":20,"sort":11}'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "u-sign": "643ff9499febb3ee34c95ffe0bb29cb0",
    "Content-Type": "application/json"  # Content-Type不能少
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())
