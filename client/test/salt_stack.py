# ################## 获取今日未采集主机名 ##################
#result = requests.get('http://www.127.0.0.1:8000/assets.html')
# result = ['c1.com','c2.com']


# ################## 远程服务器执行命令 ##################
# import subprocess
# result = subprocess.getoutput("salt 'c1.com' cmd.run  'ifconfig'")
#
# import salt.client
# local = salt.client.LocalClient()
# result = local.cmd('c2.salt.com', 'cmd.run', ['ifconfig'])