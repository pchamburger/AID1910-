"""
模拟注册登录
"""

import pymysql

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')

# 获取游标(操作数据库,执行sql语句)
cur = db.cursor()


# 注册
def register():
    name = input("用户名:")
    password = input("密码:")
    # 判断用户名是否重复
    sql_find = "select * from user where name = %s"
    cur.execute(sql_find, [name])
    result = cur.fetchone()
    if result:
        return False
    try:
        sql_register = "insert into user (name,password)  \
                       values (%s,%s)"
        cur.execute(sql_register, [name, password])
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        print(e)
        return False


# 登录
def login():
    name = input("用户名:")
    password = input("密码:")
    sql_find = "select * from user " \
               "where name = %s and password = %s"
    cur.execute(sql_find, [name, password])
    result = cur.fetchone()
    if result:
        return True


while True:
    print("""===============
1.注册    2.登录
===============
    """)
    cmd = input("输入命令:")
    if cmd == '1':
        if register():
            print("注册成功")
        else:
            print("注册失败")
    elif cmd == '2':
        if login():
            print("登录成功")
            break
        else:
            print("登录失败")
    else:
        print("我也做不到")

# 关闭数据库
cur.close()
db.close()
