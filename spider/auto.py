import requests
from bs4 import BeautifulSoup

url = 'https://www.autohome.com.cn/news/'
respones = requests.get(url=url)
respones.encoding = respones.apparent_encoding  # 字符编码，
ret = respones.text  # 返回文本
soup = BeautifulSoup(ret, features='html.parser')  # soup对象
target = soup.find(id='auto-channel-lazyload-article')  # 找id=auto-channel-lazyload-article的标签
# print(target)
li_list = target.find_all('li')  # 找到所有的li标签
# print(li_list)
for i in li_list:
    a = i.find('a')
    if a:
        url = a.attrs.get('href')
        txt = a.find('h3')
        img = a.find('img').attrs.get('src')
        print(txt.text, 'http:' + url, 'http:' + img)
        img_url = 'http:' + img
        img_ph = requests.get(url=img_url)
        import uuid

        file_name = str(uuid.uuid4()) + '.jpg'
        with open(file_name, 'wb') as f:
            f.write(img_ph.content)
