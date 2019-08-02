from sqlalchemy import Column, Table  # , ForeignKey
from sqlalchemy.sql.expression import select
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import registry, relationship, joinedload, foreign


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
    cid = Column(Integer)
    # cid = Column(ForeignKey(Card.id))
    # 如果不在模型上定义ForeignKey字段 则关系字段无需设置primaryjoin
    card = relationship(Card, primaryjoin=cid == foreign(Card.id))
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

        for i in result.scalars().unique():
            """
                如果不在模型上定义ForeignKey字段 则结果集需要使用.unique()
                when an ORM query is compiled, if it contains any joinedload() or contains_eager() of collections (not many-to-one or one-to-one), it will be required that .unique() is called on the result before iterating. 
                an error will be raised otherwise; this is because the uniquing is needed in order to get the expected objects back when joined eager loading of collections is used. this will prevent confusion over the uniquing not occurring for a joined eager load collection result.
            """
            print(dict(i))
            # 如果不在模型上定义ForeignKey字段 会访问关系字段会变成序列 哪怕是多对一
            print(dict(i.card[0]))


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
