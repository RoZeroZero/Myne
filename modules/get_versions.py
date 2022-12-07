import urllib.request
from xml.dom import minidom

def versions():
    url = "https://raw.githubusercontent.com/RoZeroZero/Myne/main/versions.xml"
    urllib.request.urlretrieve(url, 'versions.xml')
    mydoc = minidom.parse('versions.xml')
    items = mydoc.getElementsByTagName('NAME')
    for elem in items:
        print(elem.firstChild.data)
versions()