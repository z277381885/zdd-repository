# import psutil
#
# temps = psutil.sensors_temperatures()
#
# print(temps)        #返回一个字典
#
#     #输出:{'acpitz': [shwtemp(label='', current=27.8, high=119.0, critical=119.0), shwtemp(label='', current=29.8, high=119.0, critical=119.0)], 'coretemp': [shwtemp(label='Physical id 0', current=36.0, high=84.0, critical=100.0), shwtemp(label='Core 0', current=35.0, high=84.0, critical=100.0), shwtemp(label='Core 1', current=33.0, high=84.0, critical=100.0), shwtemp(label='Core 2', current=32.0, high=84.0, critical=100.0), shwtemp(label='Core 3', current=36.0, high=84.0, critical=100.0)]}
#
# cpu0_temp = temps['coretemp'][0]
# print(cpu0_temp)
#
#     #输出:shwtemp(label='Physical id 0', current=36.0, high=84.0, critical=100.0)
#
#
# print('%s: %s' % (cpu0_temp.label, cpu0_temp.current))
#
#     #输出:Physical id 0: 36.0

###########################
###--zabbix

import requests
import json

url = 'http://192.168.1.11/zabbix/api_jsonrpc.php'
                #注意api_jsonrpc.php文件所在位置,源安装包内有,
headers = {'Content-Type': 'application/json-rpc'}
                #头部信息
###获取版本###
data = {
    "jsonrpc": "2.0",               #jsonrpc版本,固定的
    "method": "apiinfo.version",    #手册上提供的
    "params": [],
    "id": 1                        #随便给数字
}       #zabbix的官网api手册上复制下来

###输出:{'jsonrpc': '2.0', 'result': '3.4.4', 'id': 101}
###zabbix的版本信息为:3.4.4

#####获取授权码
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",              #zabbix的管理员用户
#         "password": "zabbix"          #管理员用户的密码
#     },
#     "id": 1
# }
####输出:{'jsonrpc': '2.0', 'result': '561c47b7b2242a0c0d8260db7de9e47d', 'id': 1}
####授权码为:561c47b7b2242a0c0d8260db7de9e47d



###获取组信息
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 "Zabbix servers",
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": "561c47b7b2242a0c0d8260db7de9e47d",       #使用上一步查询出来的授权码
#     "id": 1
# }
###输出:{'jsonrpc': '2.0', 'result': [{'groupid': '2', 'name': 'Linux servers', 'internal': '0', 'flags': '0'}, {'groupid': '4', 'name': 'Zabbix servers', 'internal': '0', 'flags': '0'}], 'id': 1}
###的到组信息为:'groupid': '2',


###获取Template os linux模板ID
# 获取Template os linux模板ID
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#                 # "Template OS Windows"
#             ]
#         }
#     },
#     "auth": "561c47b7b2242a0c0d8260db7de9e47d",
#     "id": 1
# }

#输出为:{'jsonrpc': '2.0', 'result': [{'proxy_hostid': '0', 'host': 'Template OS Linux', 'status': '3', 'disable_until': '0', 'error': '', 'available': '0', 'errors_from': '0', 'lastaccess': '0', 'ipmi_authtype': '-1', 'ipmi_privilege': '2', 'ipmi_username': '', 'ipmi_password': '', 'ipmi_disable_until': '0', 'ipmi_available': '0', 'snmp_disable_until': '0', 'snmp_available': '0', 'maintenanceid': '0', 'maintenance_status': '0', 'maintenance_type': '0', 'maintenance_from': '0', 'ipmi_errors_from': '0', 'snmp_errors_from': '0', 'ipmi_error': '', 'snmp_error': '', 'jmx_disable_until': '0', 'jmx_available': '0', 'jmx_errors_from': '0', 'jmx_error': '', 'name': 'Template OS Linux', 'flags': '0', 'templateid': '10001', 'description': '', 'tls_connect': '1', 'tls_accept': '1', 'tls_issuer': '', 'tls_subject': '', 'tls_psk_identity': '', 'tls_psk': ''}], 'id': 1}

###模板id为:'templateid': '10001',


###创建主机
# 创建主机web2，它在2号组中，使用10001模板
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.create",
#     "params": {
#         "host": "web2",
#         "interfaces": [   # 定义通过什么方式进行监控
#             {
#                 "type": 1,  # 1号类型是zabbix agent
#                 "main": 1,
#                 "useip": 1,
#                 "ip": "192.168.1.254",
#                 "dns": "",
#                 "port": "10050"
#             }
#         ],
#         "groups": [
#             {
#                 "groupid": "2"
#             }
#         ],
#         "templates": [
#             {
#                 "templateid": "10001"
#             }
#         ],
#         "inventory_mode": 0,   # 主机资产记录
#         "inventory": {
#             "macaddress_a": "01234",
#             "macaddress_b": "56768"
#         }
#     },
#     "auth": "561c47b7b2242a0c0d8260db7de9e47d",
#     "id": 1
# }

##输出:{'jsonrpc': '2.0', 'result': {'hostids': ['10254']}, 'id': 1}
##在zabbix服务里面,添加了一台被监控主机且,hostids:10254

####获取主机信息
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 # "Zabbix server",
#                 # "Linux server"
#                 "web2"
#             ]
#         }
#     },
#     "auth": "561c47b7b2242a0c0d8260db7de9e47d",
#     "id": 1
# }

###输出为:{'jsonrpc': '2.0', 'result': [{'hostid': '10254', 'proxy_hostid': '0', 'host': 'web2', 'status': '0', 'disable_until': '1556262109', 'error': 'Get value from agent failed: cannot connect to [[192.168.1.254]:10050]: [111] Connection refused', 'available': '2', 'errors_from': '1556261344', 'lastaccess': '0', 'ipmi_authtype': '-1', 'ipmi_privilege': '2', 'ipmi_username': '', 'ipmi_password': '', 'ipmi_disable_until': '0', 'ipmi_available': '0', 'snmp_disable_until': '0', 'snmp_available': '0', 'maintenanceid': '0', 'maintenance_status': '0', 'maintenance_type': '0', 'maintenance_from': '0', 'ipmi_errors_from': '0', 'snmp_errors_from': '0', 'ipmi_error': '', 'snmp_error': '', 'jmx_disable_until': '0', 'jmx_available': '0', 'jmx_errors_from': '0', 'jmx_error': '', 'name': 'web2', 'flags': '0', 'templateid': '0', 'description': '', 'tls_connect': '1', 'tls_accept': '1', 'tls_issuer': '', 'tls_subject': '', 'tls_psk_identity': '', 'tls_psk': ''}], 'id': 1}
###查询出的主机'hostid': '10254'


r = requests.post(url,headers=headers , data = json.dumps(data))
print(r.json())         #返回值,result部分为主要信息






















