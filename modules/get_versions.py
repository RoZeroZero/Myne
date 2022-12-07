import urllib.request
name = []
uri = []
desc = []
def versions():
    if len(name)==0:
        urllib.request.urlretrieve("https://raw.githubusercontent.com/RoZeroZero/Myne/main/versions.txt", 'versions.txt')
        with open("versions.txt") as f:
            for line in f:
                print("test")
                name.append(line.split("@")[0])
                uri.append(line.split("@")[1])
                desc.append(line.split("@")[2])
    return name, uri, desc

def pack():
    return