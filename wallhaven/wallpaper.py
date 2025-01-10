"""
爬取wallhaven主页中展示的壁纸, 保存到本地
"""

import requests

from bs4 import BeautifulSoup

url = 'https://wallhaven.cc/'
# 爬取主页展示的壁纸

# 设置代理
proxies = {
    'http': 'http://127.0.0.1:7897',
    'https': 'http://127.0.0.1:7897',
}

with requests.get(url, proxies=proxies, timeout=5) as response:
    main_page = BeautifulSoup(response.text, "html.parser")

span_list = main_page.find_all('span', attrs={'class': 'sm-thumb'})

for span in span_list:
    pic_url = span.find('a').get('href')
    pic_name = pic_url.split('/')[-1]

    with requests.get(pic_url, proxies=proxies, timeout=5) as pic_response:
        pic_page = BeautifulSoup(pic_response.text, "html.parser")

    div = pic_page.find('div', attrs={'class': 'scrollbox'})
    pic = div.find('img').get('src')

    with open("downloads\\" + pic_name + '.jpg', 'wb') as f:
        f.write(requests.get(pic, proxies=proxies, timeout=5).content)

    print(pic_name + ' 下载完成')
