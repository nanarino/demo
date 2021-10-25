from threading import Thread
import asyncio
from sqlalchemy import Column, select
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import registry

url = "mysql+aiomysql://root:123456@127.0.0.1:3306/demodemo"
async_egn = create_async_engine(url)
mapper_registry = registry()
Base = mapper_registry.generate_base()


class Demo(Base):
    __tablename__ = 'demotable'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    mark = Column(String(30))

    def __repr__(self) -> str:
        return f'{self.id!r}, {self.name!r}, {self.mark!r}'


async def main():
    async with AsyncSession(async_egn) as session:
        result = await session.execute(select([Demo]))
        print(result.fetchall())

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
