data={
	'hostname': 'node2',
	'data': {
		'Server': [
			{
				'hostname': 'node2',
				'manage_ip': '172.17.1.199',
				'os_platform': 'CentOSLinux-7',
				'os_version': '7.4.1708',
				'cpu_model': 'Intel(R)Core(TM)i5-8250UCPU@1.60GHz',
				'cpu_count': 1
			},
			{
				'hostname': 'node3',
				'manage_ip': '172.17.1.188',
				'os_platform': 'CentOSLinux-7',
				'os_version': '7.4.1708',
				'cpu_model': 'Intel(R)Core(TM)i5-8250UCPU@1.60GHz',
				'cpu_count': 2
			},
			{
				'hostname': 'node4',
				'manage_ip': '172.17.1.123',
				'os_platform': 'CentOSLinux-7',
				'os_version': '7.4.1708',
				'cpu_model': 'Intel(R)Core(TM)i5-8250UCPU@1.60GHz',
				'cpu_count': 2
			},
			{
				'hostname': 'node5',
				'manage_ip': '172.17.1.14',
				'os_platform': 'CentOSLinux-7',
				'os_version': '7.4.1708',
				'cpu_model': 'Intel(R)Core(TM)i5-8250UCPU@1.60GHz',
				'cpu_count': 4
			},
			{
				'hostname': 'node6',
				'manage_ip': '172.17.1.16',
				'os_platform': 'CentOSLinux-7',
				'os_version': '7.4.1708',
				'cpu_model': 'Intel(R)Core(TM)i5-8250UCPU@1.60GHz',
				'cpu_count': 2
			},
			{
				'hostname': 'node7',
				'manage_ip': '172.17.1.189',
				'os_platform': 'CentOSLinux-7',
				'os_version': '7.4.1708',
				'cpu_model': 'Intel(R)Core(TM)i5-8250UCPU@1.60GHz',
				'cpu_count': 6
			},
			{
				'hostname': 'node8',
				'manage_ip': '172.17.1.183',
				'os_platform': 'CentOSLinux-7',
				'os_version': '7.4.1708',
				'cpu_model': 'Intel(R)Core(TM)i5-8250UCPU@1.60GHz',
				'cpu_count': 2
			},
			{
				'hostname': 'node9',
				'manage_ip': '172.17.1.18',
				'os_platform': 'CentOSLinux-7',
				'os_version': '7.4.1708',
				'cpu_model': 'Intel(R)Core(TM)i5-8250UCPU@1.60GHz',
				'cpu_count': 7
			},
			{
				'hostname': 'node10',
				'manage_ip': '172.17.1.177',
				'os_platform': 'CentOSLinux-7',
				'os_version': '7.4.1708',
				'cpu_model': 'Intel(R)Core(TM)i5-8250UCPU@1.60GHz',
				'cpu_count': '2',
			},
		],
		'Disk': {
			'DISKslot#0': {
				'capacity': '40.5GB',
				'slot': 'DISKslot#0'
			}
		},
		'Memory': {
			'RAMslot#0': {
				'capacity': '2024MB',
				'slot': 'RAMslot#0',
				'model': 'DRAM',
				'speed': 'Unknown',
				'manufacturer': 'NotSpecified',
				'sn': 'NotSpecified'
			}
		},
		'NIC': {
			'ens33': {
				'name': 'ens33',
				'hwaddr': '00: 0c: 29: a1: 2e: 67',
				'up': False,
				'netmask': '255.255.255.0',
				'ipaddrs': '172.17.1.199'
			}
		}
	}
}
for i in data['data']['Server']:
    print(i)
# print(data['hostname'])
# print(data['data']['Server'])
