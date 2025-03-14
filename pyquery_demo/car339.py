import requests

from pyquery import PyQuery as pq

session = requests.Session()

data = {
    "LoginID": "zh23j_emu",
    "Password": "abc123"
}

login_url = "https://www.car339.com/User/LogOn/"
shelf_url = "https://www.car339.com/User/Shelf"

# 登录
login = session.post(login_url, data=data)

# 获取书架信息
resp = session.get(shelf_url)
html = pq(resp.text)

books = html(".grid tr").items()

for book in books:
    items = book("td")

    title = items("a").eq(0).text()
    chapter = items.eq(2).text()
    bookmark = items.eq(3).text()
    update = items.eq(4).text()

    print(title, chapter, bookmark, update)
