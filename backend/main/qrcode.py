import cv2
import pyzbar.pyzbar as pyzbar
def scanner():
    cap= cv2.VideoCapture(0)
    Flag=True
    cnt=0
    data=''
    while Flag:
        _, frame= cap.read()
        cv2.imshow("Frame", frame)
        do=pyzbar.decode(frame)
        for ob in do:
            data=ob.data
            cnt=1
        key=cv2.waitKey(1)
        if key==27:
            break
        if cnt==1:
            return data
