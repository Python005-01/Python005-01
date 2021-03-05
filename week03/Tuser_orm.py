import pymysql
from sqlalchemy import create_engine, Table, Column, String, Integer, DateTime, Enum, or_, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy import desc
from datetime import datetime


"""
使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:
    用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
    将 ORM、插入、查询语句作为作业内容提交
"""


Base = declarative_base()

class Tuser_table(Base):
    __tablename__  = 'Tuser'
    uid = Column(Integer(), primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    age = Column(Integer())
    birthday = Column(DateTime(), default=datetime.now)
    sex = Column(Enum('男', '女'))
    education= Column(String(10), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
dburl="mysql+pymysql://testuser:testpass@127.0.0.1:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")
#Base.metadata.create_all(engine)

SessionClass = sessionmaker(bind=engine)
session = SessionClass()

#添加数据
add1 = Tuser_table(username='tom1', age=33, birthday='1987-1-1', sex='男', education='本科')
add2 = Tuser_table(username='tom2', age=39, birthday='1981-2-7', sex='男', education='专科')
add3 = Tuser_table(username='jack1', age=30, birthday='1990-3-4', sex='男', education='专科')
add4 = Tuser_table(username='jack2', age=39, birthday='1981-12-1', sex='男', education='本科')
add5 = Tuser_table(username='yuyu', age=30, birthday='1992-11-3', sex='男', education='本科')
add6 = Tuser_table(username='peter', age=29, birthday='1991-4-3', sex='女', education='本科')
add7 = Tuser_table(username='luxi', age=28, birthday='1992-11-3', sex='女', education='本科')
add8 = Tuser_table(username='kiki', age=28, birthday='1992-11-3', sex='女', education='本科')
#session.add(add1)
#session.add(add2)
#session.add(add3)
#session.add(add4)
#session.add(add5)
#session.add(add6)
#session.add(add7)
#session.add(add8)
#session.commit()


#查询数据
result = session.query(Tuser_table.username, Tuser_table.age,  func.date_format(Tuser_table.birthday, "%Y-%m-%d"), Tuser_table.sex, Tuser_table.education).all()
for i in result:
    print(i)

#排序查询根据年龄
print("排序查询")
result = session.query(Tuser_table.username, Tuser_table.age,  func.date_format(Tuser_table.birthday, "%Y-%m-%d"), Tuser_table.sex, Tuser_table.education).order_by(desc(Tuser_table.age))
for i in result:
    print(i)

#条件查询根据学历和性别
print("条件查询")
result = session.query(Tuser_table.username, Tuser_table.age,  func.date_format(Tuser_table.birthday, "%Y-%m-%d"), Tuser_table.sex, Tuser_table.education).filter(and_(Tuser_table.education == "本科", Tuser_table.sex == "男"),).all()
for i in result:
    print(i)
session.commit()