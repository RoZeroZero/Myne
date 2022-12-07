import urllib.request
from xml.dom import minidom

def versions():
    url = ""
    urllib.request.urlretrieve(url, 'temp/versions.xml')
