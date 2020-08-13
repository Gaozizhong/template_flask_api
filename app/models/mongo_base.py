"""
    @File  : mongo_base.py
    @Author: GaoZizhong
    @Date  : 2020/6/11 14:22
    @Desc  : mongo模型类
"""
import datetime

from flask_mongoengine import MongoEngine

mongo_db = MongoEngine()


class BaseModel(object):
    """
    所有模型基类
    """
    createDate = mongo_db.DateTimeField(defualt=datetime.datetime.utcnow)
    modifyDate = mongo_db.DateTimeField(defualt=datetime.datetime.utcnow)


# 津南违建表
class jhwj(BaseModel, mongo_db.Document):
    _id = mongo_db.ObjectIdField()
    content = mongo_db.StringField()
    image_name = mongo_db.StringField()
    file_number = mongo_db.StringField()
    image = mongo_db.FileField()






