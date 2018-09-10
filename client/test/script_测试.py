#采集资产：三种不同的信息
from client.conf import settings
class BasePlugin(object):
    def __init__(self):
        mode_list = ['Agent','SSH','Salt']
        if settings.MODE in mode_list:
            self.mode = settings.MODE
        else:
            raise Exception("配置文件出错")

    def ssh(self,cmd):
        pass

    def agent(self,cmd):
        pass

    def salt(self,cmd):
        pass
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
        #判断平台
        ret = self.shell_cmd("查看平台的命令")
        if ret == 'win':
           return self.window()
        elif ret == "linux":
          return  self.linux()
        else:
            raise Exception("只支持linux和window")

    def linux(self):
        raise Exception("........")
    def window(self):
        raise Exception("........")

class DiskPlugin(BasePlugin):
    def linux(self):
       output = self.shell_cmd('ifconfig')
       return output
    def window(self):
        output = self.shell_cmd('ipconfig')
        return output


obj = DiskPlugin()
result = obj.execute()