import urllib.request

def versions():
    url = "https://raw.githubusercontent.com/RoZeroZero/Myne/main/versions.xml"
    urllib.request.urlretrieve(url, 'versions.xml')

versions()