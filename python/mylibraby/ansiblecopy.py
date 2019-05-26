# 编写ansible模块
# 1、创建自定义模块路径
# [root@room8pc16 day06]# mkdir mylibraby
# export ANSIBLE_LIBRARY=/var/ftp/nsd_2018/nsd1811/devops/day06/mylibraby
# mylibraby/mycopy.py
#! /usr/bin/env python
from ansible.module_utils.basic import AnsibleModule
import shutil

def main():
    module = AnsibleModule(
        argument_spec=dict(         #是个字典
            yuan=dict(required=True, type='str'),       #创建一个自定义源,是必须填,类型是str
            mudi=dict(required=True, type='str')        #创建一个自定义目的,是必须填,类型是str
        )
    )
    shutil.copy(module.params['yuan'], module.params['mudi'])   #从自定义源拷贝到自定义的目的
    module.exit_json(changed=True)                      #退出的固定格式

if __name__ == '__main__':
    main()
# 2、测试在ansible目录里面执行
# ansible webservers -m mycopy -a "yuan=/etc/hosts mudi=/tmp/zhuji.txt"