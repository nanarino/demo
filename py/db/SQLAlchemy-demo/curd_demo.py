from sqlalchemy import *

url = "mysql+pymysql://root:123456@127.0.0.1:3306/demodemo?charset=utf8"

egn = create_engine(url)
#  如果是sqlite3 最好指定poolclass=sqlalchemy.pool.NullPool
# （或sqlalchemy.pool.SingletonThreadPool）

metadata = MetaData()
table = Table('demotable', metadata, autoload=True, autoload_with=egn)

conn = egn.connect()
#  mysql`show variables like "interactive_timeout";
#  可以查询mysql的engine.connect()超时时间 一般是8小时


# 增一条
conn.execute(insert(table).values(name="zzz", mark="你好"))

# 增批量
conn.execute(insert(table), [
    {"name": "www", "mark": "111"},
    {"name": "ddd", "mark": "222"},
])

# 删
conn.execute(delete(table).where(table.columns.id == 1))

# 改
conn.execute(update(table).where(table.columns.name == "www"))

# 查
query = select([table]).order_by(desc(table.c.id)).offset(1).limit(2)
for row in conn.execute(query):  # 也可使用fetchone和fetchall迭代
    print(row)
# table.columns 可以简写为 table.c
