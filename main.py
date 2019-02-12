import requests
import xml.etree.ElementTree as ET

r = requests.get('https://news.tut.by/rss/it.rss')

tree = ET.fromstring(r.text)

news = [el.find('title').text for el in tree.iter(tag='item')]

for item in news[:5]:
    print(item)