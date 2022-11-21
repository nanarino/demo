from sqlalchemy import Column, Table, select
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import registry

url = "mysql+aiomysql://root:123456@127.0.0.1:3306/demodemo"
async_egn = create_async_engine(url)  # 可配置连接池，默认size5max10
mapper_registry = registry()
Base = mapper_registry.generate_base()


def table(mapper: Base) -> Table:
    """表映射 转 表对象"""
    return mapper.__table__


class mapper_to_dict_able_mixin:
    '''混合继承用，转dict需要至少实现的方法'''

    def keys(self):
        return map(lambda c: c.key, table(self).columns)

    def __getitem__(self, key):
        return getattr(self, key)


class Demo(mapper_to_dict_able_mixin, Base):
    '''Demo表映射'''
    __tablename__ = 'demotable'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))


async def main():
    # 转为Table查询结果集的行可以直接转dict
    async with AsyncSession(async_egn) as session:
        result = await session.execute(select(table(Demo)))
        print(result.fetchall())
    # 使用混合继承后结果集.scalars()里的行直接转dict
    async with AsyncSession(async_egn) as session:
        result = await session.execute(select(Demo))
        # result.scalars().all()
        for i in result.scalars():
            print(dict(i))
    # 元类构造器sqlalchemy.orm.sessionmaker在作为依赖导出时推荐使用

if __name__ == "__main__":
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
