import salt.client

class Memplugin(object):
    def saltcli(self,tgt,module,args=None):
        local = salt.client.LocalClient()
        if args:
            ret = local.cmd(tgt,module,args)

        else:
            ret = local.cmd(tgt,module)

        return ret


    def linux_cmd(self):
        tgt = '*'
        module = 'cmd.run'
        args = ['dmidecode  -q -t 17 2']
        data = self.saltcli(tgt,module,args)
        return data


    def parse(self):
        data = self.linux_cmd()
        host = 'node2'
        data = data[host].split('Memory Device')   #切割返回的数据
        key_map = {
            'Size': 'capacity',
            'Locator': 'slot',
            'Type': 'model',
            'Speed': 'speed',
            'Manufacturer': 'manufacturer',
            'Serial Number': 'sn',

        }
        new_data = []
        for item in data:
            item = item.split('Total Width: 32 bits')
            for i in item:
                if i.strip() == '': #判断i去空后是不是空字符换，若果是剔除
                    continue
                else:
                    # print('开始',i.strip(),'结束')
                    if 'Size: No Module Installed' in i:
                        continue
                    else:
                       new_data.append(i.strip('\n\t').split('\n\t'))
        #print(new_data[0])
        content = {}    #men返回的字典数据
        mem_dic = {}     #返回最后的mem的字典数据
        for i in new_data[0]:
            key,values = i.split(':')
            if key in key_map:
                content[key_map[key.strip()]] = values.strip()
        #print(segment)
        mem_dic[content['slot']] = content
        return mem_dic
                





if __name__ == "__main__":
    obj = Memplugin()
    data = obj.parse()
    print(data)


