import os


v_url = 'https://raw.githubusercontent.com/RoZeroZero/Myne/main/versions.db' # version (name, version, description, short url) url
v_path = str(os.getenv('APPDATA')) + '\\.minecraft\\versions\\' # version
db = 'versions.db'
minecraft_path = os.path.abspath(os.curdir)

names = []

x_l = 5
x_r = 215
x_rd = 375
xy = '495x270' #+50x0

font='Segoe UI'
