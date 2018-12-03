import requests
import json
import cv2

def requestMessage(addr,text):
    url = addr + '/fileName'
    data = {'key': text}
    response = requests.post(url, json=data)
    print(response.text)
    return ""

def requestUpload(addr,file):
    url = addr + '/fileUpload'
    try:
        response = requests.post(url, files=file)
    finally:
        print(response.text)
    return ""

if __name__ =='__main__':
    addr = 'http://localhost:5001'
    requestMessage(addr,'hi')
    
    file = {'file':open('test.avi','rb')}
    requestUpload(addr, file)#request foward to server

