from pyquery import PyQuery as pq

url = 'https://www.zbj.com/fw/?k=saas'

doc = pq(url=url)

item_list = doc('.serve-item-im').items()

for item in item_list:
    service_name = item('.name-pic-box span').text().replace("\n", "")
    price = item('.price span').text()
    company = item('.text-overflow-line').text()

    print(service_name, price, company)
