import sys
import requests
import xml.etree.ElementTree as ET

import article
from article import Article
from article import TutArticle
from article import RedditArticle

def get_article_class(user_url):
    if 'tut' in user_url:
        return TutArticle, 'item'
    #todo add RedditArticle
    elif 'reddit' in user_url:
        return RedditArticle, 'link'
    else:
        return Article, 'article'

# TODO check if input exists
user_url = sys.argv[1]

rss = requests.get(user_url)

ArticleCls, article_tag = get_article_class(user_url)

tree = ET.fromstring(rss.text)

news = [ArticleCls(el) for el in tree.iter(tag=article_tag)]

for item in news[:5]:
    print(item)
