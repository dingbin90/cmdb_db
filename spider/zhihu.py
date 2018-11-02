import requests
from bs4 import BeautifulSoup
url = 'https://www.zhihu.com/signup?next=%2F'
ise = requests.Session()
resp = ise.get(url=url,
               headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                        }
               )
soup = BeautifulSoup(resp.text,features='html.parser')
# xsrf_arg = soup.find(name='input',attrs={'name': '_xsrf'})
# valume = xsrf_arg.get('value')
# print(valume)
print(soup)
print(resp.cookies)