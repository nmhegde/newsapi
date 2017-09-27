### NewsApi - A wrapper around newsapi.org api

#### How to install ?

```sh
git clone git@github.com:nmhegde/newsapi.git && cd newsapi
sudo python setup.py install
```

#### How to use ?

```sh
from newsapi import News
news = News("<Your API Key")
news.load_sources()
news.load_articles()
```

#### Where do I refer API documentation ?
[newsapi.org's documentation](https://newsapi.org/#documentation)
