import os


version_id_url = 'https://raw.githubusercontent.com/RoZeroZero/Myne/main/versions.db'
db = 'versions.db'
minecraft_path = os.getenv('APPDATA') + '\\myne'

names = []

x_l = 5
x_r = 215
x_rd = 375
xy = '495x270' #+50x0

ico = 'assets/myne.ico'

font='Minecraft Rus'

# def update():
#         with open('versions.zip', 'wb') as f:
#             response = requests.get(version_id_url, stream=True)
#             total_length = response.headers.get('content-length')

#             if total_length is None: # no content length header
#                 f.write(response.content)
#                 return False
#             else:
#                 dl = 0
#                 total_length = int(total_length)
#                 for data in response.iter_content(chunk_size=int(total_length/100)):
#                     dl += len(data)
#                     f.write(data)
#                     percent = int(100 * dl / total_length)
#                 return True