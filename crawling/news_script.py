# coding=utf-8
'some comment...'
__author__ = 'Jiateng Liang'

import requests
import json
from news import get_news_by_nid, News
from bootstrap_init import db

tag_map = ['bitcoin', 'blockchain', 'litecoin', 'ethereum', 'bitcoin-scams', 'ripple', 'altcoin', 'bitcoin-regulation',
           'monero']
url = 'https://cointelegraph.com/api/v1/content/json/_tp'


def insert_news(news, tag):
    obj = News()
    obj.tag = tag
    obj.title = news['title']
    obj.url = news['url']
    obj.author = news['author_title']
    obj.date = news['date']
    obj.img = news['img']
    obj.thumb = news['thumb']
    obj.retina = news['retina']
    obj.n_id = news['id']
    db.session.add(obj)
    db.session.commit()


for tag in tag_map:
    for page in range(1, 1000):
        param = {
            'page': page,
            'lang': 'en',
            '_token': 'K17ONZw41qKORvz1BUA0M6F0kEZv45MH6BwiXsVL',
            'tag': tag,
        }
        res = requests.post(url, data=param)
        try:
            json_obj = json.loads(res.text)
            recent_news = json_obj['posts']['recent']
            for news in recent_news:
                news_in_db = get_news_by_nid(news['id'])
                if news_in_db is None:
                    insert_news(news, tag)
        except Exception as e:
            print e
