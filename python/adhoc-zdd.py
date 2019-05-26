#!/usr/bin/env python

import json
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
import ansible.constants as C
'''
最终版
1,加上函数
2,将一些目录,主机组,执行的命令改成变量

'''

def adhoc(sources, hosts, module, args):

    '''
    #connection='local' 连接方式:
    #module_path=['/to/mymodules'] 定义模块位置,执行指令,例如-m shell除了搜索ansible默认的模块,还会到这个指定地方取搜索模块
    #forks=10  指定启动的进程数量
    #become=None 如果要使用普通用户远程登录服务器,指定要变成管理员方式,例如是由su还是sudo
    #check=False, 不真正执行,语言将要发生的变化
    #diff=False     执行
    '''
    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='ssh', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

    #DataLoader() 用于查找并解析yml json ini文件,把他们转换成python的数据类型,----可查看笔记的yuml详细解析
    loader = DataLoader() # Takes care of finding and reading yaml, json and ini files
    passwords = dict()
    # passwords = dict(vault_pass='secret')


    #定义主机清单,可以将各主机用逗号隔开的字符串,也可以指定文件路径列表
    #sources=['/root/ansible/hosts']  主机列表文件目录
    inventory = InventoryManager(loader=loader, sources=sources)
    # inventory = InventoryManager(loader=loader, sources=['/root/ansible/hosts'])
    # inventory = InventoryManager(loader=loader, sources='localhost,')  原语句
    variable_manager = VariableManager(loader=loader, inventory=inventory)


    play_source =  dict(                   #创建一个执行源
            name = "Ansible Play",         #play的名字
            hosts = hosts,        #指定在哪些主机上执行命令,实际中有webservers主机组
            # hosts = 'webservers',  # 指定在哪些主机上执行命令,实际中有webservers主机组
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module=module, args=args), register='shell_out'),
                # module = module       #调用的模块
                # args = args           #执行的命令
                # dict(action=dict(module='shell', args='ls'), register='shell_out'),
                # dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
             ]
        )

    #通过上面的配置创建一个play,
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    #创建任务管理器,执行play
    tqm = None
    try:
        tqm = TaskQueueManager(
                  inventory=inventory,
                  variable_manager=variable_manager,
                  loader=loader,
                  options=options,
                  passwords=passwords,
              )
        result = tqm.run(play)
    finally:
        if tqm is not None:
            tqm.cleanup()

        shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)

if __name__ == '__main__':
    sources = ['/root/ansible/hosts']
    hosts = 'webservers'
    module = 'shell'
    args = 'mkdir -p /tmp/aaa/bbb'
    adhoc(sources, hosts, module, args)
