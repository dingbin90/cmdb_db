from client.src.plugins.salt_serverinfo import Serverplugin
from client.src.plugins.salt_nic import Nicplugin
from client.src.plugins.salt_mem import Memplugin
from client.src.plugins.salt_disk import DiskPlugin
import salt.client
class Clectdata(Serverplugin):
    def hostlist(self):
        local = salt.client.LocalClient()
        data = local.cmd('*','test.ping')
        hostlist = list(data.values())
        return hostlist

    def celedata(self):
        data = {}
        data['node2']={}
        print('__________')
        Server_data = Serverplugin().parse(self)
        #Nic_data = Nicplugin.parse(self)
        #Mem_data = Memplugin.parse(self)
        #Disk_data = DiskPlugin.parse(self)
        data['node2']['Server'] = Server_data
        #data['node2']['Disk'] = Disk_data
        #data['node2']['Memory'] = Mem_data
        #data['node2']['NIC'] = Nic_data
        return data



if __name__ == "__main__":
    obj = Clectdata()
    data = obj.celedata()
    print(data)

