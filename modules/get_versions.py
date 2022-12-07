import urllib.request

def versions():
    url = "https://raw.githubusercontent.com/RoZeroZero/Myne/main/versions.txt"
    urllib.request.urlretrieve(url, 'versions.txt')
    with open("versions.txt") as f:
        for line in f:
            print(line)
versions()