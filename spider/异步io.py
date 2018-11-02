import socket
import select
#
#sk = socket.socket()

# #连接
# sk.connect(('www.baidu.com',80)) #io阻塞
# print("......连接成功")
# #发送数据
# sk.send(b'GET / HTTP/1.0\r\nHost:www.baidu.com\r\n\r\n')
# #等待响应，返回数据
# data = sk.recv(1024) #io阻塞
# print(data)
# sk.close()

class Httprequest:
    def __init__(self,sk,host):
        self.socket = sk
        self.host = host
    def fileno(self):
        return self.socket.fileno()


class AsynRequest:
    def __init__(self):
        self.conn = []
        self.connection = []
    def add_request(self,host):
        try:
            sk = socket.socket()
            sk.setblocking(0)
            sk.connect((host,443))
        except BlockingIOError as e:
            pass
        request = Httprequest(sk,host)
        self.conn.append(request)
        self.connection.append(request)

    def run(self):
        while True:
            r_list,w_list,e_list = select.select(self.conn,self.connection,self.conn,0.05)   #select  监听数据变化
            for w in w_list:
                #只要能循环到，说明socket和服务器连接成功
                print(w.host,'连接成功')
                content = 'GET / HTTP/1.0\r\nHost:%s\r\n\r\n'% (w.host)
                print(content)
                w.socket.send(bytes(content,encoding='utf-8'))
                self.connection.remove(w)
            for r in r_list:
                #r是HTTPrequest对象，
                recv_data = bytes()
                
                while True:
                    try:
                        data = r.socket.recv(1024)
                        recv_data+=data
                    except Exception as e:
                        break
                print(r.host,'返回数据。。。。。',recv_data,)
                r.socket.close()
                self.conn.remove(r)
            if len(self.conn) == 0:
                break




url_list = [
    'www.baidu.com',
    'cn.bing.com',
    'www.cnblogs.com',

]

req = AsynRequest()
for url in url_list:
    req.add_request(url)



req.run()