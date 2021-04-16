import dropbox

class TransferData:
    def __init__(self, accessToken):
        self.access_token = accessToken
    
    def uploadFiles(self, fileFrom, fileTo):
        print(fileFrom)
        dropb = dropbox.Dropbox(self.access_token)
        File = open(fileFrom , 'rb')
        dropb.files_upload(File.read(), fileTo)

def start():
    accessToken = 'sl.AvBAspQH5B8UaxPp6BLC7TvI-HAxdZqK0y3zklhvQ2bcH1jXXS8UODeRiCOeeIwge6T5fjYF2_nibdRKTh7_Vu8nGz5gE9jGrtCGbdATwVwpZP5vil-FHLnUsYGaHACvJ5QCx-gCamg'
    storage = TransferData(accessToken)
    fileFrom = input("Please enter the file you want to upload:   ")
    fileTo = input("Please enter the path name to upload the file:   ")
    storage.uploadFiles(fileFrom,fileTo)
    print("File is uploaded")

start()