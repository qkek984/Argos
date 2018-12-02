import requests
import json
import cv2

def requestMessage(addr,text):
    url = addr + '/fileName'
    data = {'key': text}
    response = requests.post(url, json=data)
    print(response.text)
    
if __name__ =='__main__':
    addr = 'http://localhost:5001'
    requestMessage(addr,'hi')
    
