import salt.client

class Nicplugin(object):
    def saltcli(self,tgt,module,args=None):
        local = salt.client.LocalClient()
        if args:
            ret = local.cmd(tgt,module,args)
        else:
            ret = local.cmd(tgt,module)

        return ret


    def linux_cmd(self):
        tgt = '*'
        module = 'network.interfaces'
        data = self.saltcli(tgt,module)
        return data

    def parse(self):
        data = self.linux_cmd()
        host = 'node2'
        data[host].pop('lo')
        #print(data)
        nic_info = {}
        nic_name = list(data[host].keys())[0]
        #print(nic_name)
        nic_info['name'] = nic_name
        nic_info['hwaddr'] = data[host][nic_name]['hwaddr']
        nic_info['status'] = data[host][nic_name]['up']
        nic_info['netmask'] = data[host][nic_name]['inet'][0]['netmask']
        nic_info['ipaddrs'] = data[host][nic_name]['inet'][0]['address']
        return nic_info


if __name__ == "__main__":
    obj = Nicplugin()
    nic_info = obj.parse()
    print(nic_info)


