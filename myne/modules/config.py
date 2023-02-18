import os


version_id_url = 'https://raw.githubusercontent.com/RoZeroZero/Myne/main/versions.db'
db = 'versions.db'
minecraft_path = os.path.abspath(os.curdir)

names = []

x_l = 5
x_r = 215
x_rd = 375
xy = '495x270' #+50x0

ico = 'assets/myne.ico'

font='Segoe UI'

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

# def listbox_versions_click(event):
#     frame.button_work['text'] = 'Choose'
#     frame.button_work['state'] = ['active']
#     cs = frame.listbox_versions.curselection()
#     try:
#         if cs[0]>=0: 
#             index = cs[0]frame.listbox_versions.curselection()
#             read_description(index)
#             if check_version(index)==True:
#                 frame.button_work['text'] = 'Play'
#             else: frame.button_work['text'] = 'Download'
#     except Exception:
#         frame.button_work['state'] = ['disabled']
