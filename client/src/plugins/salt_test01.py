from client.src.plugins.salt_serverinfo import Serverplugin
from client.src.plugins.salt_nic import Nicplugin
from client.src.plugins.salt_mem import Memplugin
from client.src.plugins.salt_disk import DiskPlugin

def celedata():
    data = {}
    data['hostname']='node2'
    data['data']={}
    Server_data = Serverplugin().parse()
    Nic_data = Nicplugin().parse()
    Mem_data = Memplugin().parse()
    Disk_data = DiskPlugin().parse()
    data['data']['Server'] = Server_data
    data['data']['Disk'] = Disk_data
    data['data']['Memory'] = Mem_data
    data['data']['NIC'] = Nic_data
    return data
    #print(data)

if __name__ == "__main__":
    celedata()
