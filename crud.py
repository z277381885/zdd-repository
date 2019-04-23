from SqlAlchemy import Departments, Employees, Salary, Session

session = Session()         #创建session
#######插入一条数据
hr = Departments(dep_id=1, dep_name='人事部')
session.add(hr)     #将hr添加到session

# session.commit
# session.close
###解释:
# hr为变量, Departments,为创建表时候的表对象,可查看SqlAlchemy.py文件,再插入对应的值

########插入多条数据
# ops = Departments(dep_id=2, dep_name='运维部')
# dev = Departments(dep_id=3, dep_name='开发部')
# qa = Departments(dep_id=4, dep_name='测试部')
# finance = Departments(dep_id=5, dep_name='财务部')
# ui = Departments(dep_id=6, dep_name='设计部')
# session.add_all([ops, dev, qa, finance, ui])
#######插入多条数据
# yc = Employees(
#     emp_id = 1,
#     emp_name = '杨晨',
#     email = 'yc@163.com',
#     dep_id = 2
# )
# zyp = Employees(
#     emp_id = 2,
#     emp_name = '郑云鹏',
#     email = 'zyp@163.com',
#     dep_id = 2
# )
# lzj = Employees(
#     emp_id = 3,
#     emp_name = '李注江',
#     email = 'lzj@163.com',
#     dep_id = 2
# )
# cyj = Employees(
#     emp_id = 4,
#     emp_name = '陈益建',
#     email = 'cyj@qq.com',
#     dep_id = 1
# )
# hqp = Employees(
#     emp_id = 5,
#     emp_name = '黄勤品',
#     email = 'hqp@tarena.com',
#     dep_id = 3
# )
# zds = Employees(
#     emp_id = 6,
#     emp_name = '赵东升',
#     email = 'zds@.tedu.cn',
#     dep_id = 3
# )
# cd = Employees(
#     emp_id = 7,
#     emp_name = '陈栋',
#     email = 'cd@tedu.cn',
#     dep_id = 4
# )
# session.add_all([yc, zyp, lzj, cyj, hqp, zds, cd])

#############################
# query1 = session.query(Departments)  # 将class作为参数，返回实例
# # print(query1)                      # query1只是个sql语句
# deps = query1.all()                  # 取出查询的全部结果
# # print(deps)                           # deps是由 数据库表每行记录生成的实例 构成的列表
# for dep in query1:
#     print(dep.dep_id, dep.dep_name)
#############################
# query2 = session.query(Employees)
# print(query2)                           #未切片.返回的是sql语句
# print(query2.all())                     #返回的是实例构成的列表
# for emp in query2:
#     print(emp.emp_id, emp.emp_name, emp.email)
#############################
# ##将类变量作为参数，返回值是元组***
# query3 = session.query(Employees.emp_name, Employees.email)
# print(query3)
# print(query3.all())                         #返回的是元组组成的列表
# for name, email in query3:
#     print(name, email)
############-------排序查询
# query4 = session.query(Employees).order_by(Employees.emp_id)
# print(query4)                              #取的是sql语句
# for emp in query4:
#     print(emp.emp_id, emp.emp_name, emp.email)
############------切片查询
###取切片时,涉及到了值,所以下面query5不再是sql语句,而是实例构成的列表
# query5 = session.query(Departments).order_by(Departments.dep_id)[2:5]
# print(query5)                                         #取的不是sql语句,而是实例构成的列表
# for dep in query5:
#     print(dep.dep_id,dep.dep_name)
###########-----过滤查询
# query6 = session.query(Departments).filter(Departments.dep_id<=3)
# print(query6)                           #返回查询语句
# for dep in query6:
#     print(dep.dep_id, dep.dep_name)

##########------模糊查询
# query7 = session.query(Employees).filter(Employees.email.like('%.cn'))
# print(query7)
# for emp in query7:
#     print(emp.emp_name,emp.email)

#########-----in
# query8 = session.query(Employees).filter(Employees.dep_id.in_([1,3]))
# print(query8)
# for emp in query8:
#     print(emp.emp_name,emp.dep_id)

#########----in--取反加 ~
# query9 = session.query(Employees).filter(~Employees.dep_id.in_([1,3]))
# print(query9)
# for emp in query9:
#     print(emp.emp_name,emp.dep_id)
########----and_ 和 or_--需要单独导入
# from sqlalchemy import and_,or_
# query10 = session.query(Departments) \
#     .filter(and_(Departments.dep_id>=2,Departments.dep_id<6))
# print(query10)
# for dep in query10:
#     print(dep.dep_id , dep.dep_name)
#
# query11 = session.query(Departments) \
#     .filter(or_(Departments.dep_id<=2))

######---统计查询
# query12 = session.query(Departments).count()
# print(query12)

#####---多表查询
# query13 = session.query(Employees.emp_name,Departments.dep_name)\
#     .join(Departments)
# for emp_name,dep_name in query13:
#     print(emp_name,dep_name)
##--注意join里面的内容,谁在后就join谁
# query14 = session.query(Departments.dep_name, Employees.emp_name)\
#     .join(Employees)
# for emp_name ,dep_name in query14:
#     print(emp_name,dep_name)

#####---字段更新
# query15 = session.query(Departments).filter(Departments.dep_name=='人事部')
# print(query15.all())    #返回的是长度为1的列表

# print(query15.all()[0])       #同下一样
# print(query15.one())          #返回的是实例,同上一样
# hr = query15.one()
# print(hr)                     #将实例赋值给'hr'
# print(hr.dep_name)            #输出'人事部'
# hr.dep_name ='人力资源部'       #将人事部修改成了'人力资源部'
#####---删除一条记录
# query16 = session.query(Departments).filter(Departments.dep_id==6)
# ui = query16.one()
# session.delete(ui)

session.commit()
session.close()
























