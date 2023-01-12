from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.expression import select
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import registry, relationship, joinedload


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


class Card(mapper_to_dict_able_mixin, Base):
    __tablename__ = 'card'
    id = Column(Integer, primary_key=True)
    username = Column(String(63))
    password = Column(String(63))
    is_active = Column(Integer)


class Card_bindinfo(mapper_to_dict_able_mixin, Base):
    __tablename__ = "card_bindinfo"
    id = Column(Integer, primary_key=True)
    cid = Column(ForeignKey(Card.id))
    card = relationship(Card)
    tbr_name = Column(String(255))
    tbr_id_type = Column(String(255))
    tbr_id_num = Column(String(255))
    tbr_sex = Column(String(255))
    tbr_birth = Column(String(255))
    tbr_age = Column(Integer)
    tbr_email = Column(String(255))
    tbr_tel = Column(String(255))
    tbr_addr = Column(String(255))
    bbr_is_tbr = Column(String(255))
    bbr_name = Column(String(255))
    bbr_id_type = Column(String(255))
    bbr_id_num = Column(String(255))
    bbr_sex = Column(String(255))
    bbr_birth = Column(String(255))
    bbr_age = Column(Integer)
    bbr_email = Column(String(255))
    bbr_tel = Column(String(255))
    bbr_addr = Column(String(255))
    effect_date = Column(String(255))


async def main():
    async with AsyncSession(async_egn) as session:
        result = await session.execute(
            select(Card_bindinfo).options(
                joinedload(Card_bindinfo.card, innerjoin=True)
            ).where(Card_bindinfo.id == 1)
        )

        for i in result.scalars():
            print(dict(i), dict(i.card))

        """ # 也可以使用select.join_from。他们都需要在模型上定义ForeignKey字段
            # 官方文档：https://docs.sqlalchemy.org/en/14/tutorial/orm_related_objects.html#tutorial-orm-related-objects
            
            result = await session.execute(
                select(Card).join_from(Card, Card_bindinfo).where(Card_bindinfo.id == 1)
            )

            for i in result.scalars():
                print(dict(i))
        """


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
