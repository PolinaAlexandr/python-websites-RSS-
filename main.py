import sys
import requests
import xml.etree.ElementTree as ET

import article
from article import Article, TutArticle, HabrArticle


def get_article_class(user_url):
    if 'tut' in user_url:
        return TutArticle, 'item'
    elif 'habr' in user_url:
        return HabrArticle, 'item'
    else:
        return Article, 'article'

# TODO check if input exists
user_url = sys.argv[1]

rss = requests.get(user_url)

ArticleCls, article_tag = get_article_class(user_url)

tree = ET.fromstring(rss.text)

news = [ArticleCls(el) for el in tree.iter(tag=article_tag) if el]


for item in news[:5]:
    print(item)
