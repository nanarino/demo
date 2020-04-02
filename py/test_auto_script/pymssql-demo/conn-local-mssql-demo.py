"""
连接本地MSSQL数据库连接 使用Windows账号登录 并执行查询语句
"""

from pprint import pprint
import pymssql

DATABASES = {
    'default': {
        "host": '127.0.0.1',
        "database": "demo_project",
    },
}


def conn_create(name='default'):
    conn = pymssql.connect(**DATABASES[name])
    cursor = conn.cursor()
    if not cursor:
        raise Exception("*" * 32 + "数据库连接失败" + "*" * 32)
    else:
        print("*" * 32 + "数据库连接成功" + "*" * 32)
    return (cursor, conn)


cur, conn = conn_create()

cur.execute('select * from sys.tables')
"""
conn.commit() #修改数据后提交事务
"""

#querylist = cur.fetchone()
querylist = cur.fetchall()

pprint(querylist, width=60, compact=True)

conn.close()
