from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import threading
from lib import sha256
from server import client
global savecam

class saveCam:
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
        self.out = cv2.VideoWriter('file/'+fileName+'.avi',self.fourcc, 20.0, self.size)
        
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

class checkTime(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.addr = 'http://localhost:5001'
    def run(self):
        global savecam
        #init
        fileName=time.strftime("%y%m%d_%H:%M:%S",time.localtime())
        fileName=sha256.encrypt_string(fileName)
        savecam.updateFileName(str(fileName))

        #request foward to server
        client.requestMessage(self.addr, str(fileName))

        while True:
            time.sleep(300)# 5분간 슬립
            fileName=time.strftime("%y%m%d_%H:%M:%S",time.localtime())
            fileName=sha256.encrypt_string(fileName)
            savecam.updateFileName(str(fileName))
            client.requestMessage(self.addr, str(fileName))
            

if __name__=='__main__':
    timeTread=checkTime()
    savecam=saveCam()
    timeTread.start()
    savecam.save()
    
    
