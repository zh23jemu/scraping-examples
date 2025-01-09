import re

import requests

'''
爬取dy2018首页, 必看热片的片名和下载链接
'''

url = "https://www.dy2018.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}

with requests.get(url, headers=headers) as response:
    response.encoding = "gbk"
    sourcePage = response.text

obj1 = re.compile(r'必看热片.*?<ul>(?P<url>.*?)</ul>', re.S)
result1 = obj1.search(sourcePage)

urls = result1.group("url").strip()

obj2 = re.compile(r"<li><a href='(?P<sublink>.*?)' title", re.S)
result2 = obj2.finditer(urls)

obj3 = re.compile(r'◎片　　名　(?P<name>.*?)<br />.*?'
                  r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)

for i in result2:
    with requests.get(url + i.group("sublink"), headers=headers) as sub_response:
        sub_response.encoding = "gbk"
        sub_page = sub_response.text

    result3 = obj3.search(sub_page)
    print(result3.group("name"), result3.group("download"))
