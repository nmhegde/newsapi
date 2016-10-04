import pickle
import redis

from newsapi.news import News
news = News("5264a435358e4a64b511e662d206f288")

r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('news', pickle.dumps(news))
