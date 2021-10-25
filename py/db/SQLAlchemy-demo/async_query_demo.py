from threading import Thread
from sqlalchemy import *
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine

metadata = MetaData()

table = Table(
    "demotable",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('mark', String(30)),

)

url = "mysql+aiomysql://root:123456@127.0.0.1:3306/demodemo"
async_egn = create_async_engine(url)


async def main():
    '''async with async_egn.connect() as conn:
        result = await conn.execute(select([table]))
        print(result.fetchall())'''
    
    async with async_egn.connect() as conn:
        async_result = await conn.stream(select([table]))
        async for row in async_result:
            print(row)

# loop.run_until_complete() / asyncio.run(main())
# 大概率提前关闭导致报错时使用以下代码在另一个线程启动

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