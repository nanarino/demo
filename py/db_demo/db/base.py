from abc import ABCMeta#, abstractmethod

class __cur_vc(metaclass=ABCMeta):
    """游标虚拟类

        内部方法不要求实现
    """
    def __init__(self, *args, **kwargs):
        pass

    def execute(self, sql:str):
        """执行SQL语句

            未实现
        """
        raise NotImplementedError

    def executemany(self, sql:str, args:list):
        """执行多条嵌入了模板的SQL语句"""
        for i in args:
            self.execute(sql%i)

    def fetchone(self):
        """吐出执行SQL语句的结果的第一条（下一条）数据

            未实现
        """
        raise NotImplementedError

    def fetchall(self):
        """吐出执行SQL语句的结果的全部数据

            但是已被fetchone吐出的数据不会再出现
        """
        while data_row:=self.fetchone():
            yield tuple(data_row)

    def callproc(self, proc_name:str, args:tuple):
        """执行存储过程
        
            未实现
        """
        raise NotImplementedError


class __conn_vc(metaclass=ABCMeta):
    """连接虚拟类

        内部方法不要求实现
    """
    
    def close(self):
        """关闭连接

            未实现
        """
        raise NotImplementedError
    
    def commit(self):
        """提交修改

            未实现
        """
        raise NotImplementedError

    def cursor(self, *args, **kwargs):
        return __cur_vc(*args, **kwargs)


class db_vmodule(metaclass=ABCMeta):
    """数据库虚拟模块
    
        内部方法不要求实现
    """
    def connect(self,*args,**kwargs):
        return __conn_vc(*args,**kwargs)


class Generic_db_base(metaclass=ABCMeta):
    """数据库整合基类
    
        init_args:
            db_type: 数据库模块
            info: 数据库连接信息，包含hosts，password等

        Attributes:
            db_type：数据库模块，实例化前缺省值
            default_args：数据库连接信息，实例化前缺省值
    """
    default_args = dict()
    db_type = db_vmodule

    def __init__(self, info:dict=dict(), db_type=None):
        """实例化数据库基类
        
            Args:
                db_type: 数据库模块
                info: 数据库连接信息，包含hosts，password等
        """
        if info:
            self.default_args = info
        if db_type:
            self.db_type = db_type
        conn = self.db_type.connect(**self.default_args)
        self.conn = conn
        self.cur = conn.cursor()

    def close(self):
        self.conn.close()

    def execute(self, sql):
        return self.cur.execute(sql)

    def commit(self):
        self.conn.commit()


class fetch_Mixin():
    """混入需要fetch方法才能获取查询结果的类"""
    def execute(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()