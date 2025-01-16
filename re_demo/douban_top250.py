"""
豆瓣会将获取大量内容的IP认定为异常IP,
如果出现此错误, 考虑使用代理或隔几天再试
"""


import re

import requests

url = "https://movie.douban.com/top250"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}

f = open("豆瓣电影top250.csv", "w", encoding="utf-8")

for p in range(0, 250, 25):
    params = {
        "start": p,
        "filter": ""
    }

    with requests.get(url, headers=headers, params=params) as response:
        sourcePage = response.text

    # re.S参数使.*?可以匹配换行符
    obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>'
                     r'.*?<p class="">.*?导演: (?P<director>.*?)&nbsp;'
                     r'.*?<br>(?P<year>.*?)&nbsp;'
                     r'.*?<span class="rating_num" property="v:average">(?P<rating_num>.*?)</span>'
                     r'.*?<span>(?P<rating_people>.*?)人评价</span>'
                     , re.S)

    result = obj.finditer(sourcePage)

    for i in result:
        f.write(
            f"{i.group('name')},{i.group('director')},{i.group('year').strip()},{i.group('rating_num')},{i.group('rating_people')}\n")

f.close()
