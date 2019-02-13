import requests
import urllib.request
import xml.etree.ElementTree as ET

import article
from article import TutArticle
from article import RedditArticle

m = urllib(str(input))
r = urllib.requests.get(m)
if r.find("tut") is True:
    tree = ET.fromstring(r.text)
    news = [TutArticle(el) for el in tree.iter(tag='item')]

elif r.find("reddit") is True:
    tree = ET.fromstring(r.text)
    news = [RedditArticle(el) for el in tree.iter(tag='entry')]

else:
    # tree = ET.fromstring(r.text)
    # news = [article(el) for el in tree.iter(tag=str(input))]
    pass


for item in news[:5]:
    print(item)