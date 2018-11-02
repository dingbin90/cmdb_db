#爬91信息
import requests
from bs4 import BeautifulSoup
for i in range(1,500):
    #print(i)
    url = 'http://g.p03.space/forumdisplay.php?fid=19&page='+str(i)
    #print(url)
    ret = requests.get(url=url)
    ret.encoding = ret.apparent_encoding
    #print(ret.text)
    soup = BeautifulSoup(ret.text,features='html.parser')
    r1 = soup.find(id='moderate')
    tb = r1.find('table')
    tbd_list = tb.find_all('tbody')
    #print(tbd_list)
    for tbd in tbd_list:
        th = tbd.find('th')
        a = th.find('a')
        if a:
            if '合肥' in a.text:
                a_url = a.attrs.get('href')
                a_txt = a.text
                #print('http://g.p03.space/' + a_url, a_txt)
                a_txt = 'http://g.p03.space/' + a_url +'信息'+a.text
                with open('信息.txt','a',encoding='utf-8') as f:
                    f.write(a_txt)



