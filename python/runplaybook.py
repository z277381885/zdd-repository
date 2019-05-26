from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor
        #PlaybookExecutor用于调用playbook的模块

#具体参考ansible常用属性与官方源代码,这里是纵向排列,上面是横向排列而已
Options = namedtuple(
    'Options',
    [
        'connection',
        'remote_user',
        'ask_sudo_pass',
        'verbosity',
        'ask_pass',
        'module_path',
        'forks',
        'become',
        'become_method',
        'become_user',
        'check',
        'listhosts',
        'listtasks',
        'listtags',
        'syntax',
        'sudo_user',
        'sudo',
        'diff'
    ]
)                       #以上为选项
options = Options(
    connection='smart',
    remote_user=None,
    ask_pass=None,
    sudo_user=None,
    forks=5,
    sudo=None,
    ask_sudo_pass=False,
    verbosity=5,
    module_path=None,
    become=None,
    become_method=None,
    become_user=None,
    check=False,
    diff=False,
    listhosts=None,
    listtasks=None,
    listtags=None,
    syntax=None
)                   #以上为实例化
loader = DataLoader()   #分析yuml,ini等文件
passwords = dict()      #密码认证,免密模式
inventory = InventoryManager(loader=loader,	sources=['/root/ansible/hosts'])
                        #InventoryManager定义主机清单参数,sources是hosts主机群文件
variable_manager = VariableManager(loader=loader, inventory=inventory)

def	runpb(pb_path):                 #用于执行playbook函数
    playbook = PlaybookExecutor(
        playbooks=pb_path,                  #playbook的路径
        inventory=inventory,                #上面定义了主机清单
        variable_manager=variable_manager,  #意思是参数在哪?在上面定义的56行
        loader=loader,                      #什么方式分析文件,前面已定义 52行
        options=options,                    #选项,前面已定义
        passwords=passwords
    )       #调用PlaybookExecutor用于执行playbook的函数
    result = playbook.run()
    return result

if __name__ == '__main__':
    runpb(pb_path=['/root/ansible/yum.yml'])     #传入实现写好的yml文件绝对路径,

'''
此程序作用是定义主机hosts文件,定义yml文件(playbook文件),即可使用本程序来调用playbook来实现ansible管理
'''
