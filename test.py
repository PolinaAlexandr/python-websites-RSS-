import xml.etree.ElementTree as ET

with open ('test.xml') as o:
    tree = ET.parse(o)

for n in tree.findall('body'):
    print(n)
    
print(tree.getroot())
print (n.text)

# url = n.attrib.get('xm')
# root = ET.fromstring(test)
# root.findall(".")
# root.findall()