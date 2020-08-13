"""
    @File  : pg_base.py
    @Author: gaozizhong
    @Date  : 2020/6/12 14:02
    @Desc  : postgres基础的模型类：存放所有表共有的字段
"""
from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from geoalchemy2 import Geometry
from lin.exception import NotFound
from sqlalchemy import Column


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class Query(BaseQuery):
    """覆盖查询类：自定义一些查询方法"""
    # def filter_by(self, **kwargs):
    #     if 'is_delete' not in kwargs.keys():
    #         kwargs['is_delete'] = 0
    #     return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident, **kwargs):
        rv = self.get(ident)
        if not rv:
            raise NotFound()
        return rv

    def first_or_404(self, **kwargs):
        rv = self.first()
        if not rv:
            raise NotFound()
        return rv


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    # create_by = Column(Integer)
    # update_time = Column('update_time', Integer)

    gid = Column(db.Integer, primary_key=True)
    geom = Column(Geometry(geometry_type='POLYGON', srid=4548))
    # is_delete = Column(SmallInteger, default=0)
    # create_time = Column('create_time', db.Integer, default=int(datetime.now().timestamp()))

    def __getitem__(self, item):
        # dict()时可以配合Keys方法使用
        return getattr(self, item)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    # @property
    # def create_datetime(self):
    #     """把时间戳转换成日期格式"""
    #     if self.creat_time:
    #         return datetime.fromtimestamp(self.creat_time)
    #     else:
    #         return None

    # def delete(self):
    #     """删除一条数据"""
    #     self.is_delete = 1

    def hide(self, *keys):
        """隐藏字段"""
        for key in keys:
            self.fields.remove(key)
        return self

    def append(self, *keys):
        """添加字段"""
        for key in keys:
            self.fields.append(key)
        return self
