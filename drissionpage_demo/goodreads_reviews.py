import time
import re

from DrissionPage import ChromiumPage

url = 'https://www.goodreads.com/book/show/243900/reviews?reviewFilters=eyJhZnRlciI6Ik5URTFMREUwTXpnNU5qazJPRE13TURBIn0%3D'


def handle_data(data):
    clean_text = re.sub(r'<[^>]+>', '', data)  # 去除所有HTML标签
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()  # 合并多余空格
    return clean_text

def single_line(data):
    return ' '.join(data.split())


page = ChromiumPage()
page.listen.start('/graphql')
page.get(url)

# 一开始有好几个匹配的请求, 可以通过结果筛选
for _ in range(4):
    res = page.listen.wait()
    try:
        data = res.response.body['data']['getReviews']['edges']
        with open('reviews.txt', 'w', encoding='utf-8') as f:
            for item in data:
                item = single_line(item['node']['text'])
                f.write(item + '\n')
    except Exception as e:
        pass

# 点得太快会加载不出来
time.sleep(2)
page('@text()=Show previous reviews').click()

res = page.listen.wait()
data = res.response.body['data']['getReviews']['edges']
print(data)

# 将data中的每个元素的text写入txt文件
with open('reviews.txt', 'w', encoding='utf-8') as f:
    for item in data:
        item = single_line(item['node']['text'])
        f.write(item + '\n')

# 然后是加载后面的评论
while True:
    page('@text()=Show more reviews').click()
    time.sleep(2)
    res = page.listen.wait()
    data = res.response.body['data']['getReviews']['edges']
    print(data)
    # 将data中的每个元素的text写入txt文件
    with open('reviews.txt', 'a', encoding='utf-8') as f:
        for item in data:
            item = single_line(item['node']['text'])
            f.write(item + '\n')
