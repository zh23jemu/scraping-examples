import requests

from lxml import etree

url = 'http://en.most-famous-paintings.com/MostFamousPaintings.nsf/ListOfTop1000MostPopularPainting?OpenForm'
prefix = 'https://en.most-famous-paintings.com/MostFamousPaintings.nsf/'
domain = "https://en.most-famous-paintings.com"

with requests.get(url) as response:
    html = response.text
et = etree.HTML(html)

divs = et.xpath('//div[@class="mosaicflow__item"]')

sub_response = None
for div in divs:
    sub_url = div.xpath('./a/@href')

    sub_response = requests.get(prefix + sub_url[0])
    sub_html = sub_response.text

    sub_et = etree.HTML(sub_html)
    image_source = sub_et.xpath('//img[@id="ArtworkImageZoom"]/@src')[0]

    print(domain + image_source)

sub_response.close()
