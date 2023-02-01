import urllib.request

name = []
uri = []
desc = []
class get:
    def update(self):
        try:
            urllib.request.urlretrieve("https://raw.githubusercontent.com/RoZeroZero/Myne/main/versions.txt", 'versions.txt')
            with open("versions.txt") as f:
                for line in f:
                    name.append(line.split("@")[0])
                    uri.append(line.split("@")[1])
                    desc.append(line.split("@")[2])
        except:
            pass
        return name, uri, desc

def pack(id):
    urllib.request.urlretrieve("https://www.dropbox.com/s/" + uri[id] + "/" + name[id] + ".zip?dl=1", name[id] + ".zip")
