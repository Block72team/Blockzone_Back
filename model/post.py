# coding=utf-8
'Article model'
import datetime

__author__ = 'Jiateng Liang'
from sqlalchemy import Column, BigInteger, String, Text, DateTime, Boolean
from bootstrap_init import db


class Post(db.Model):
    __tablename__ = 'posts'
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    title = Column(String(256), nullable=False)
    category_id = Column(BigInteger, nullable=False)
    tag_ids = Column(String(256), nullable=False, default='[]')
    likes = Column(BigInteger, nullable=False, default=0)
    pv = Column(BigInteger, nullable=False, default=0)
    image_header_id = Column(BigInteger, nullable=False)
    content = Column(Text, nullable=False)
    author = Column(String(50), nullable=False)
    region = Column(String(50), nullable=True)
    is_ad = Column(Boolean, nullable=False, default=False)
    create_time = Column(DateTime, nullable=False, default=datetime.datetime.now())
    update_time = Column(DateTime, nullable=False, default=datetime.datetime.now())
