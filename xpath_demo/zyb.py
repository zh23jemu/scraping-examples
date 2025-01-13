import requests

from lxml import etree

url = 'https://www.zbj.com/fw/?k=saas'

with requests.get(url) as response:
    html = response.text

# print(html)

et = etree.HTML(html)

divs = et.xpath('//div[@class="search-result-list-service"]/div')

for div in divs:
    price = div.xpath('./div//div[@class="price"]/span/text()')[0]
    company = div.xpath('./div//div[@class="shop-info text-overflow-line"]/text()')[0]
    title = div.xpath('./div//a[@class="serve-name text-overflow-line-two oneline"]/span//text()')
    print(''.join(title), price, company)
