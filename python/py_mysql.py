# import pymysql
#
#
# conn = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     passwd='123qqq...AAA',
#     db='nsd1811',
#     charset='utf8'
# )                    #创建连接
#
# cursor = conn.cursor()          #创建游标,查询数据默认为元组类型
#
# ##sql语句
# # create_dep = '''create table departments(
# # dep_id INT ,dep_name VARCHAR(20),PRIMARY KEY (dep_id)
# # )'''
# # cursor.execute(create_dep)      #执行sql语句
#
# # create_emps = '''create table employees(
# # emp_id INT ,emp_name VARCHAR(20), email VARCHAR(50),dep_id INT,
# # PRIMARY KEY (emp_id),FOREIGN KEY (dep_id) REFERENCES departments(dep_id)
# # )'''
# # cursor.execute(create_emps)
#
# create_sal='''create table salary(
# auto_id INT ,emp_id INT , date DATE ,basic INT , awards INT ,
# PRIMARY key(auto_id), FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
# )'''
# cursor.execute(create_sal)      #execute只能插一项  executemany可插入多项
#
# # create_dep = '''create table employees(
# # emp_id INT,
# # emp_name VARCHAR(20),
# # email VARCHAR(50),
# # dep_id INT ,
# # PRIMARY KEY (emp_id),FOREIGN KEY(dep_id) REFERENCES departments(dep_id)
# # )'''
# # cursor.execute(create_dep)      #执行sql语句
# conn.commit()                   #提交改动
# cursor.close()                  #关闭游标
# conn.close()                    #关闭连接

###
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123qqq...AAA',
    db='nsd1811',
    charset='utf8'
)                    #创建连接

cursor = conn.cursor()          #创建游标,查询数据默认为元组类型

##sql语句
#########插入数据
# insert_dep1='insert  into departments VALUES (%s, %s)'
# deps = [(1,'人事部'),(2,'运维部'),(3,'开发部'),(4,'市场部')]
# cursor.executemany(insert_dep1,deps)      #execute只能插一项  executemany可插入多项
# deps2 = [(7,'运营部'),]
# cursor.executemany(insert_dep1,deps2)      #execute只能插一项  executemany可插入多项
# deps3 = [(6,'财务部'),(7,'运营部')]
# cursor.executemany(insert_dep1,deps3)      #execute只能插一项  executemany可插入多项
#########更新修改数据
# update_hr = 'update departments set dep_name=%s WHERE dep_name=%s'
# data = ('人力资源部' , '人事部')
# cursor.execute(update_hr,data)
##########删除数据
# del_yy = 'delete from departments WHERE dep_name = %s'
# yy_dep = ('运营部')
# cursor.execute(del_yy,yy_dep)
##########查询数据
# select1 = 'select * from departments ORDER by dep_id'
# cursor.execute(select1)             #运行语句
# result1 = cursor.fetchone()         #取一行记录
# result2 = cursor.fetchmany(2)       #取指定数量的记录,有指针,接着上面记录后面取
# result3 = cursor.fetchall()         #取全部数据,接着上面指针取出数据
# print(result1)               #输出:(1, '人力资源部')
# print(result2)              #输出:((2, '运维部'), (3, '开发部'))
# print(result3)              #输出:((4, '市场部'), (5, '测试部'), (6, '财务部'))
#########游标,取出指定数据
# select2 = 'select * from departments ORDER by dep_id'
# cursor.execute(select2)             #运行语句
# cursor.scroll(3,mode = 'absolute')  #以绝对方式指针从第1条向下移动3条记录到第4条
# result1 = cursor.fetchone()         #取出一条数据,指针指向下一条,第5条
# cursor.scroll(-1)                   #指针默认以相对方式移动,接着上面,在第5条基础上,指针向上移动一条
# result2 = cursor.fetchone()         #取出一条数据,指针指向下一条,第5条
# result3 = cursor.fetchone()         #取出一条数据,指针指向下一条,第6条
# print(result1)                  #输出:(4, '市场部')
# print(result2)                  #输出:(4, '市场部')
# print(result3)
# ###################
#
# conn.commit()                   #提交改动
# cursor.close()                  #关闭游标
# conn.close()                    #关闭连接

################