from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide
import sys

# https://python-dependency-injector.ets-labs.org/

class Db:
    def __init__(self, config: dict):
        self.config = config
        ...


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    db = providers.Singleton(Db, config=config.db)


@inject
class Service:
    def __init__(self, db: Db = Provide[Container.db]):
        self.db = db
        ...


if __name__ == '__main__':
    container = Container()
    container.wire(modules=[sys.modules[__name__]])

    # auto
    from pathlib import Path
    container.config.from_ini(Path.cwd() / Path('config.ini'))
    s = Service()
    print(s.db.config)

    # override
    from unittest import mock
    with container.db.override(mock.Mock()):
        s = Service()
        print(s.db.config)