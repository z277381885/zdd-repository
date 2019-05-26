from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer ,String,ForeignKey,Date
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    'mysql+pymysql://root:123qqq...AAA@127.0.0.1/tedu1811?charset=utf8',
    encoding = 'utf8',
    # echo = True
)
# 创建引擎，根据数据库类型，选择适当的连接方式
# mysql+pymysql://用户名:密码@服务器/数据库?参数
# echo=True，调试模式，屏幕上打印操作详情，生产环境需要关闭

Base = declarative_base()                   #创建ORM映射类的基类
Session = sessionmaker(bind=engine)         #创建会话类,绑定引擎 新建的crud.py用的上

class Departments(Base):                        #定义表对象
    __tablename__='departments'                 #指定该类与哪个表对应,departments为要创建的表名
    dep_id = Column(Integer,primary_key=True)   #表结构,设置dep_id字段,并设置为主键
    dep_name = Column(String(20),unique=True)   #表结构,设置dep_id字段,属性为唯一,不能重复

class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer,primary_key=True)
    emp_name = Column(String(20))
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))
                                        #dep_id设置为外键,参考于departments表中的dep_id

class Salary(Base):
    __tablename__ = 'sqlary'
    auto_id = Column(Integer,primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer,ForeignKey('employees.emp_id'))
    baisc = Column(Integer)
    awards = Column(Integer)


if __name__ == '__main__':
    Base.metadata.create_all(engine)        #如果上面的表已存在,不会再创建

# ###成功屏幕将会显示创建过程:
# ......
# 2019-04-23 11:08:20,822 INFO sqlalchemy.engine.base.Engine {}
# 2019-04-23 11:08:20,823 INFO sqlalchemy.engine.base.Engine ROLLBACK
# 2019-04-23 11:08:20,824 INFO sqlalchemy.engine.base.Engine           ###echo=True，调试模式 的原因
# CREATE TABLE departments (
# 	dep_id INTEGER NOT NULL AUTO_INCREMENT,
# 	dep_name VARCHAR(20),
# 	PRIMARY KEY (dep_id),
# 	UNIQUE (dep_name)
# )
# 2019-04-23 11:08:20,824 INFO sqlalchemy.engine.base.Engine {}
# 2019-04-23 11:08:21,087 INFO sqlalchemy.engine.base.Engine COMMIT





















