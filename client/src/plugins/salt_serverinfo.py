import salt.client

class Serverplugin(object):
    def salt_cli(self,tgt,modules,args=None):
        cli = salt.client.LocalClient()
        if args:
            ret = cli.cmd(tgt,modules,args)
        else:
            ret = cli.cmd(tgt,modules)
        return ret

    def linux_cmd(self):
        tgt = "*"
        modules = "grains.items"
        ret = self.salt_cli(tgt,modules)
        return ret

    def parse(self):
        data = self.linux_cmd()
        print(data)
        host = 'node2'
        data = data[host]
        server_info = {}
        server_info['hostname'] = data['fqdn']
        server_info['manage_ip'] = data['ipv4'][1]
        server_info['os_platform'] = data['osfinger']
        server_info['os_version'] = data['osrelease']
        server_info['cpu_model'] = data['cpu_model']
        server_info['cpu_count'] = data['num_cpus']
        return server_info
# #
# if __name__ == "__main__":
#     obj = Serverplugin()
#     server_info = obj.parse()
#     print(server_info)
