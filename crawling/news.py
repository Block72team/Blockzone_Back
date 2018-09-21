# coding=utf-8
'some comment...'
__author__ = 'Jiateng Liang'

from sqlalchemy import Column, Integer, String, DateTime, Text
from bootstrap_init import db


class News(db.Model):
    __tablename__ = 'news_crawling'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    tag = Column(String(100), nullable=True)
    title = Column(String(255), nullable=True)
    url = Column(Text, nullable=True)
    author = Column(String(50), nullable=True)
    date = Column(String(50), nullable=True)
    content = Column(Text, nullable=True)
    img = Column(Text, nullable=True)
    thumb = Column(Text, nullable=True)
    retina = Column(Text, nullable=True)
    n_id = Column(Integer, nullable=True)


def get_news_by_nid(nid):
    return News.query(News.n_id == nid).first()

