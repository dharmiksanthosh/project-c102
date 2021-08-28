import dropbox
import cv2
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)

    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret, frame = videoCaptureObject.read()
        img_name = "snapshots/img"+str(number)+".png"

        cv2.imwrite(img_name, frame)
        start_time = time.time()
        result = False
        
    return img_name
    print('Snapshot Taken')
        
    videoCaptureObject.relese()

    cv2.destroyAllWindows()

def uploadFiles(img_name):

    access_token = 'TCYlKVKoX2IAAAAAAAAAAd90Fq97xnJQ1rg_3jqaqAnN378Gi1GEmj8GDLE68SaT'
    file = img_name
    file_f = file
    file_t = '/Whjr/c102/'+(img_name)

    dbx = dropbox.Dropbox(access_token)
    with open(file_f, 'rb') as f:
        dbx.files_upload(f.read(),file_t,mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():

    while(True):
        if((time.time()-start_time)>=5):
            name = take_snapshot()
            uploadFiles(name)
main()
