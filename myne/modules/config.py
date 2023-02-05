version_id_url = "https://raw.githubusercontent.com/RoZeroZero/ModpackLoader/master/versions.txt"
# version_id_url = "https://www.dropbox.com/s/2my8gi447rd10pg/Cosmo_1.12.2.zip?dl=1"


global percent

x_l = 5
x_r = 165
x_rd = 325
xy = '445x270'

ico = "assets/myne.ico"

font="Minecraft Rus"

def update():
        with open("versions.zip", "wb") as f:
            response = requests.get(version_id_url, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None: # no content length header
                f.write(response.content)
                return False
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=int(total_length/100)):
                    dl += len(data)
                    f.write(data)
                    percent = int(100 * dl / total_length)
                return True