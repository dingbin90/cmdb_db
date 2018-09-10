# import salt.client as sc
#
# local = sc.LocalClient()
# #ret = local.cmd('*','network.interfaces')
# ret = local.cmd('*','cmd.run',['dmidecode  -q -t 17 2'])
#
# #print(ret)
# host = '172.17.1.199'
#
# #print(type(ret[host]))
# data = ret[host].split('Memory Device')
# #print(data)
# key_map = {
#             'Size': 'capacity',
#             'Locator': 'slot',
#             'Type': 'model',
#             'Speed': 'speed',
#             'Manufacturer': 'manufacturer',
#             'Serial Number': 'sn',
#
#         }
# nuw_data = []
# for item in data:
#     item = item.split('Total Width: 32 bits')
#     for i in item:
#         if not i:
#             continue
#         else:
#  #       print('开始',i.strip(),'结束')
#             if 'Size: No Module Installed' in i:
#                 continue
#             else:
#                nuw_data.append(i)
#     # if 'Total Width: Unknown' in item:
#     #     nuw_data1.append(item)
#     # else:
#     #     nuw_data.append(item)
# print(nuw_data)
# segment = {}
#
# # for i in item:
# #     if
# #     # if len(i)>1:
#     #     i = i[1]
#     #     print(i)
#     #     if 'Data Width: Unknown' in i:
#     #         continue
#     #     else:
#     #         nuw_data.append(i)
#     # else:
#     #     nuw_data.append(i)
#  #   print(nuw_data)
#
# for i in item:
#     #print(i.strip())
#     lines = i.strip().split('\n\t')
#
#     for line in lines:
#        # print(line)
#         if len(line.split(':')) > 1:
#             key,value = line.split(':')
#         else:
#             key = line.split(':')
#             value = ''
#
#             if key in key_map:
#                 print(key)
# #         if  key in key_map:
# #             print('####3333')
# # #             segment[key_map[key.strip()]] = value.strip()
# # # print(segment)
#
#
#
#
#
# # data = ret[host]
# # name = data.keys()
# # name =list(name)[0]
# #
# # print(data[name]['inet'][0])
# # for nic,valu in data.items():
# #     print(nic,valu)


import salt.client
local = salt.client.LocalClient(
)
ret = local.cmd('*','test.ping')
hostlist = list(ret.keys())
print(type(hostlist))
for i in hostlist:
    print(i)
