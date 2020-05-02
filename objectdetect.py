import cv2
import pandas as pd
import time
from datetime import datetime
times=[]
status_list=[None,None]
df=pd.DataFrame(columns='Begin End'.split())
cap=cv2.VideoCapture(0)
first_frame=None

while True:
    check,frame = cap.read()
    status=0
    gray1=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray1,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue
    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_frame=cv2.threshold(delta_frame,40,255,cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)

    (_,cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour)<500:
            continue
        status=1
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

    status_list.append(status)
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

        
    cv2.imshow('gray',gray)
    cv2.imshow('first_frame',first_frame)
    cv2.imshow('delta_frame',delta_frame)
    cv2.imshow('thresh_frame',thresh_frame)
    cv2.imshow('frame',frame)

    key=cv2.waitKey(1)

    if key==ord('1'):
        times.append(datetime.now())
        break
print(status_list)
print(times)

for i in range(0,len(times),2):
    df=df.append({'Begin':times[i],'End':times[i+1]},ignore_index=True)
df.to_csv('times.csv')

cap.release()
cv2.destroyAllWindows


        
