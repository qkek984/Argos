from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import threading
from lib import sha256
from lib import client
global Camera

class Camera:
    def __init__(self):
        self.size=(320,240)
        #pi camera
        self.camera = PiCamera()
        self.camera.resolution = self.size
        self.camera.framerate = 40
        self.camera.brightness = 55
        self.rawCapture = PiRGBArray(self.camera, size=self.size)
        #opencv
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out=None

    def updateFileName(self,fileName):
        self.out = cv2.VideoWriter('localRepository/'+fileName+'.avi',self.fourcc, 20.0, self.size)
        
    def save(self):
        # Define the codec and create VideoWriter object
        for frame in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
            frame = frame.array
            self.out.write(frame)#save
            self.rawCapture.truncate(0)
            cv2.imshow('frame',frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release everything if job is finished
        cap.release()
        out.release()
        cv.destroyAllWindows()

class connectServer(threading.Thread):
    def __init__(self,addr,savePeriod):
        threading.Thread.__init__(self)
        self.addr = addr
        self.savePeriod= savePeriod
    def run(self):
        global camera
        first=True
        while True:
            if first == False:
                preFileName=fileName
            
            fileName=time.strftime("%y%m%d_%H:%M:%S",time.localtime())
            fileName=sha256.encrypt_string(fileName)
            camera.updateFileName(str(fileName))
            if first==True:
                first=False
                time.sleep(self.savePeriod)
                continue
            
            client.requestMessage(self.addr, str(preFileName))#request foward to server
            file = {'file':open('localRepository/'+preFileName+'.avi','rb')}
            client.requestUpload(self.addr, file)#request foward to server
            time.sleep(self.savePeriod)


if __name__=='__main__':
    cServer=connectServer(addr='http://localhost:5001',savePeriod=10)
    camera=Camera()
    
    cServer.start()
    camera.save()
