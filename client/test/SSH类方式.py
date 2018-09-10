import paramiko
import requests

##########获取今日采集主机名#########3333
# result = requests.get('http://127.0.0.1:8000/asset.html')
# result = ['c1.com','c2.com']  #比如主机名是这样的

##########通过paramiko连接远程服务器，执行命令############33
#创建SSH对象
ssh = paramiko.SSHClient()
#允许连接不再know_hosts文件的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接服务器
ssh.connect(hostname='172.17.1.8',port=22,username='root',password='123')
#执行命令
stdin,stdout,stderr = ssh.exec_command('df')
result = stdout.read()
print(result)

#关闭连接

ssh.close()


#格式话result数据


#########发送数据#####################33
#发送数据
# requests.post('http://127.0.0.1/asset.html',data=date_dic)
