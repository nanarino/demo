from sqlalchemy import *
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool

async def query():
    metadata = MetaData()
    sync_url = "mysql+pymysql://root:123456@127.0.0.1:3306/demodemo"
    sync_egn = create_engine(sync_url, poolclass=NullPool)
    table = Table('demotable', metadata, autoload=True, autoload_with=sync_egn)
    url = "mysql+aiomysql://root:123456@127.0.0.1:3306/demodemo"
    async_egn = create_async_engine(url)
    async with async_egn.connect() as conn:
        result = await conn.execute(select([table]))
        print(result.fetchall())
    async with async_egn.connect() as conn:
        async_result  = await conn.stream(select([table]))
        async for row in async_result:
            print(row)
          

asyncio.run(query())
'''
# loop.run_until_complete() / asyncio.run() 
# 提前关闭导致报错时使用以下代码在另一个线程启动
def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()
async def end_loop():
    loop = asyncio.get_event_loop()
    loop.stop()
from threading import Thread
new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()
asyncio.run_coroutine_threadsafe(query(),new_loop)
import time
time.sleep(3)
asyncio.run_coroutine_threadsafe(end_loop(),new_loop)
t.join()
'''