import requests
import xml.etree.ElementTree as ET

from article import TutArticle

r = requests.get('https://news.tut.by/rss/it.rss')

tree = ET.fromstring(r.text)

news = [TutArticle(el) for el in tree.iter(tag='item')]

for item in news[:5]:
    print(item)