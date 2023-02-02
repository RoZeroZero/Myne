import urllib.request
from progressbar import *
from config import *



name = []
uri = []
desc = []


class get:


    def check(self):
        try:
            f = open(version_id_path, "r")
        except Exception as file_error:
            print(file_error)
            return False
        f.close()
        return True

    def update(self, block_num, block_size, total_size):
        print("download")
        print(block_num)
        print(block_size)
        print(total_size)
        if block_num * block_size < total_size:
            print(block_num * block_size)
        else: print("vse")

    def __call__(self, block_num, block_size, total_size):
        get.update(self, block_num, block_size, total_size)


urllib.request.urlretrieve(version_id_url, 'versions.txt', get())

# urllib.request.urlretrieve("https://www.dropbox.com/s/" + uri[id] + "/" + name[id] + ".zip?dl=1", name[id] + ".zip")

