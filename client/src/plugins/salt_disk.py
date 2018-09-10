import salt.client

class DiskPlugin(object):
    def salt(self,tgt,module,args=None):
        local = salt.client.LocalClient()
        if args:
            ret = local.cmd(tgt,module,args)
        else:
            ret = local.cmd(tgt,module)
        return ret

    def linux_cmd(self):
        tgt = '*'
        module = 'disk.usage'
        ret = self.salt(tgt,module)
        return ret



    def parse(self):
        disk_info = {}
        data = self.linux_cmd()
        path_list = ['/run','/dev','/sys/fs/cgroup','/run/user/0','/boot','/dev/shm','/']
        disk_capacity = 0
        for arg in path_list:
            # disk_info = data['172.17.1.199'][arg]['1K-blocks']
            disk_capacity = disk_capacity + int(data['node2'][arg]['1K-blocks'])
            capacity = str(disk_capacity//1048576) + 'GB'
            disk_info['capacity'] = capacity
        return disk_info
if __name__ == "__main__":
    obj = DiskPlugin()
    data = obj.parse()
    print(data)


