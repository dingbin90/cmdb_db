from .base import BasePlugin

class DiskPlugin(BasePlugin):
    def linux(self):
       filter_keys = ['Manufacturer', 'Serial Number', 'Product Name', 'UUID', 'Wake-up Type']
       respon = ''
       for key in filter_keys:
           cmd = "dmidecode -t system|grep %s" %key
           output = str(self.shell_cmd(cmd),encoding="utf8")
           respon+=output
       return respon


    def window(self):
        output = self.shell_cmd('ipconfig')
        return output
