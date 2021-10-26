from sqlalchemy import Column, MetaData, Table, select
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.asyncio import create_async_engine

metadata = MetaData()
# 表声明
table = Table(
    "demotable",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
)

url = "mysql+aiomysql://root:123456@127.0.0.1:3306/demodemo"
async_egn = create_async_engine(url)  # 可配置连接池，默认size5max10


async def main():
    # 普通方式 结果集支持fetch系列以及one、all、first等
    async with async_egn.connect() as conn:
        result = await conn.execute(select(table))
        print(result.fetchall())
    # 流方式 结果集是异步生成器，除了fetch也可以使用async for遍历
    async with async_egn.connect() as conn:
        result = await conn.stream(table.select())
        # result.fetchall()
        async for row in result:
            print(dict(row))
    # 元类构造器sqlalchemy.orm.sessionmaker在作为依赖导出时推荐使用

if __name__ == "__main__":
    # loop.run_until_complete() / asyncio.run(main())
    # 大概率提前关闭导致报错时使用以下代码在另一个线程启动
    from threading import Thread
    import asyncio

    def start_loop(loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    async def end_loop(timeout=15):
        await asyncio.sleep(timeout)
        loop = asyncio.get_event_loop()
        loop.stop()

    new_loop = asyncio.new_event_loop()
    t = Thread(target=start_loop, args=(new_loop,))
    t.start()
    asyncio.run_coroutine_threadsafe(main(), new_loop)
    asyncio.run_coroutine_threadsafe(end_loop(3), new_loop)
    t.join()
