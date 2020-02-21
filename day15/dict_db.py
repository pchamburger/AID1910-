"""

"""

import pymysql
import re

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')

# 获取游标(操作数据库,执行sql语句)
cur = db.cursor()

# 打开文件
fd = open('dict.txt')

# 执行sql语句
sql = "insert into words (单词,单词解释) values (%s,%s);"

# 字符串分割法获取单词和解释
# for line in fd:
#     tuple_word = line.split(' ')
#     means = ' '.join(tuple_word[1::]).strip()
#     try:
#         cur.execute(sql, [tuple_word[0], means])
#         db.commit()
#     except Exception as e:
#         db.rollback()
#         print(e)

# 正则表达式获取单词和解释
for line in fd:
    tuple_word = re.findall(r'(\S+)\s+(.*)', line)[0]
    try:
        cur.execute(sql, tuple_word)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)

# 关闭数据库
cur.close()
db.close()
