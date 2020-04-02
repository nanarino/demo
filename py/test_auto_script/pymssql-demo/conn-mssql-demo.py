"""
连接指定地址的MSSQL数据库连接 使用sa身份登录 并执行查询语句
"""

from pprint import pprint
import pymssql

DATABASES = {
    'default': {
        "host": '192.168.10.1\\cbp',
        "user": "sa",
        "database": "demo_project",
        "password": "********"
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

cur.execute('select top 5 * from nnr_t1')
"""
conn.commit() #修改数据后提交事务
"""

#querylist = cur.fetchone()
querylist = cur.fetchall()

pprint(querylist, width=60, compact=True)

conn.close()
