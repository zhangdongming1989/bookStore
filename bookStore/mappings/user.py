# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, TIMESTAMP

from bookStore import db

class User(db.Model):
    """
    登录会员表
    """
    __table_name__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255))
    nickname = Column(String(255))
    realname = Column(String(255))
    password = Column(String(255))
    question = Column(String(255))
    answer = Column(String(255))
    gender = Column(String(255))
    mail = Column(String(255))
    phone = Column(String(255))
    qq = Column(String(255))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
