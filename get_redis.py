import pickle
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
news = pickle.loads(r.get('news'))

for article in news.articles:
    print article.source, article.sortBy, len(article.articles)
