import pymysql
from sqlalchemy import create_engine, Table, Column, String, Integer, DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


"""
张三给李四通过网银转账 100 极客币，现有数据库中三张表：

一张为用户表，包含用户 ID 和用户名字，
另一张为用户资产表，包含用户 ID 用户总资产，
第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。

请合理设计三张表的字段类型和表结构；
请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，
张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性
用户表
"""


Base = declarative_base()

# 用户表
class Users_table(Base):
    __tablename__  = 'users'
    uid = Column(Integer(), primary_key=True)
    username = Column(String(20), nullable=False, unique=True)

# 用户资产表
class Assets_table(Base):
    __tablename__  = 'userassets'
    id = Column(Integer(), primary_key=True)
    zid = Column(Integer(), ForeignKey(Users_table.uid))
    username = Column(String(20), nullable=False, unique=True)
    assetsnum = Column(Integer(), default=0)

# 审计用表
class Audit_table(Base):
    __tablename__  = 'audit'
    id = Column(Integer(), primary_key=True)
    transfer_time = Column(DateTime(), default=datetime.now)
    # 被转用户
    username_in = Column(String(20), nullable=False, unique=True)
    # 被转用户id
    inid = Column(Integer(), ForeignKey(Users_table.uid))
    # 转账用户
    username_out = Column(String(20), nullable=False, unique=True)
    # 转账用户id
    outid = Column(Integer(), ForeignKey(Users_table.uid))
    transfer_amount = Column(Integer())

# 用户操作类
class User_actions():
    def __init__(self):
        self.dburl = "mysql+pymysql://testuser:testpass@127.0.0.1:3306/testdb?charset=utf8mb4"
        self.engine = create_engine(self.dburl, echo=True, encoding="utf-8")

    # 转账操作
    def Transfer_deposite(self,oname, iname, nums):
        SessionClass = sessionmaker(bind=self.engine)
        session = SessionClass()
        user_out = oname
        user_in = iname
        # 查询转账用户id
        zz_user = session.query(Users_table.username, Users_table.uid).filter(Users_table.username == user_out).first()
        # 获取转账用户id
        zz_num = int(zz_user[1])

        # 查询被账用户id
        bz_user = session.query(Users_table.username, Users_table.uid).filter(Users_table.username == user_in).first()
        # 获取被转用户id
        bz_num = int(bz_user[1])

        # 转账用户出账操作
        zz_user_ssets = session.query(Assets_table.username, Assets_table.zid, \
                                     Assets_table.assetsnum).filter(Assets_table.zid == zz_num)
        zz_user_ssets.update({Assets_table.assetsnum: int(zz_user_ssets.first()[2])-nums})
        print(zz_user_ssets.first())

        # 被账用户进账操作
        bz_user_ssets = session.query(Assets_table.username, Assets_table.zid, \
                                      Assets_table.assetsnum).filter(Assets_table.zid == bz_num)
        bz_user_ssets.update({Assets_table.assetsnum: int(bz_user_ssets.first()[2]) + nums})
        print(bz_user_ssets.first())

        #记录到转账审计表
        auditadd=Audit_table(username_out=oname, username_in=iname, outid=zz_num, inid=bz_num, transfer_amount=nums)
        session.add(auditadd)
        res = session.query(Audit_table.outid, Audit_table.username_out, Audit_table.inid,\
                      Audit_table.username_in, Audit_table.transfer_amount, Audit_table.transfer_amount).all()
        print(" -----------转账审计审计表 数据表(audit)")
        for i in res:
            print(i)
        print(" -----------转转用户资产表 数据表(userassets)：", zz_user_ssets.first())
        print(" -----------被转用户资产表 数据表(userassets): ", bz_user_ssets.first())
        #session.flush()
        session.commit()
    # 添加用户
    def user_add(self, usadd):
        SessionClass = sessionmaker(bind=self.engine)
        session = SessionClass()
        session.add(usadd)
        session.commit()

    # 添加用户资产
    def assets_add(self, asadd):
        SessionClass = sessionmaker(bind=self.engine)
        session = SessionClass()
        session.add(asadd)
        session.commit()

dburl="mysql+pymysql://testuser:testpass@127.0.0.1:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")
#Base.metadata.create_all(engine)

#增加用户
"""
add_h1 = Users_table(uid=100, username='tom1')
add_h2 = Users_table(uid=101, username='tom2')
add_h3 = Users_table(uid=102, username='jack1')
add_h4 = Users_table(uid=103, username='jack2')
uadd = User_actions()
uadd.user_add(add_h1)
uadd.user_add(add_h2)
uadd.user_add(add_h3)
uadd.user_add(add_h4)
"""
#增加用户资产
""""
add_z1 = Assets_table(zid=100, username='tom1', assetsnum=2000 )
add_z2 = Assets_table(zid=101, username='tom2', assetsnum=2000)
add_z3 = Assets_table(zid=102, username='jack1', assetsnum=2000)
add_z4 = Assets_table(zid=103, username='jack2', assetsnum=2000)
zadd= User_actions()
zadd.assets_add(add_z1)
zadd.assets_add(add_z2)
zadd.assets_add(add_z3)
zadd.assets_add(add_z4)
"""
#用户转账
zzuser = User_actions()
zzuser.Transfer_deposite('tom1', 'jack1', 100)