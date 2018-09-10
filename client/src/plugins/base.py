from client.conf import settings
import paramiko
import salt.client
class BasePlugin(object):
    def __init__(self):
        mode_list = ['Agent','SSH','Salt']
        if settings.MODE in mode_list:
            self.mode = settings.MODE
        else:
            raise Exception("配置文件出错")

    def ssh(self,cmd):
        #########通过paramiko连接远程服务器，执行命令############33
        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 允许连接不再know_hosts文件的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname='172.17.1.8', port=22, username='root', password='123')
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        return result
        print('------->',result)
        # 关闭连接
        ssh.close()

    def agent(self,cmd):
        pass

    def salt(self,tgt,module,args):
        local = salt.client.LocalClient()
        if args:

            ret = local.cmd(tgt,module,args)
        else:
            ret = local.cmd(tgt,module)
        return ret

    def shell_cmd(self,cmd):
        if self.mode == "SSH":
           ret = self.ssh(cmd)

        elif self.mode == "Salt":
           ret = self.salt(cmd)

        else:
            self.mode == "Agent"
            ret = self.agent(cmd)
        return ret

    def execute(self):
        cmd = "uname -a | awk '{print $1}'"
        #判断平台
        ret = str(self.shell_cmd(cmd),encoding="utf8").strip().lower()
        # print("------->",ret)
        if ret == "linux":
            return self.linux()
        else:
            raise Exception("只支持linux和window")
    def linux(self):
        pass
        # print('((((((((((()))))))))))')
       # raise Exception("........")
    def window(self):
        raise Exception("........")
