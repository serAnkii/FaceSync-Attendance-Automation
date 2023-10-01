from sklearn.neighbors import KNeighborsClassifier
import pickle
import numpy
import os
import cv2
import csv
import time
from datetime import datetime

#for speaking 

from win32com.client import Dispatch

def speak(str1):
    speak = Dispatch(("SAPI.spVoice"))
    speak.speak(str1)

output = cv2.VideoCapture(0)
faces = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")


with open("data/faces_dataset.pkl", "rb") as f:
    FACES = pickle.load(f)

with open("data/names.pkl", "rb") as f:
    LABLES = pickle.load(f)


knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(FACES,LABLES)

bg = cv2.imread('data/image.jpg')


#working with csv file

colNames = ['Name','Date','Time']

while True:
    ok, frame = output.read()
    grayscalimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    facedata = faces.detectMultiScale(grayscalimg, 1.3, 5)  # threshold value

    # get coordinates
    for x, y, w, h in facedata:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)

        # : means all number of channels.
        cropped = frame[y : y + h, x : x + w, :]

        resize = cv2.resize(cropped, (40, 40)).flatten().reshape(1,-1)
        oput =  knn.predict(resize)
        timeobj = time.time()
        date = datetime.fromtimestamp(timeobj).strftime('%d-%m-%Y')
        timestmp = datetime.fromtimestamp(timeobj).strftime('%H:%M:%S')

        #check for the presence of file
        present = os.path.isfile("attendence/attendence_ +" + str(date) + '.csv')    


        cv2.putText(frame,str(oput[0]),(x,y-15),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(0,0,0),2)
        attendence = [str(oput[0]),str(date),str(timestmp)]
    bg[162:162 + 480,455:455 + 640] = frame
    cv2.imshow("window",bg)
    keybinding = cv2.waitKey(1)  # infinite time

    if keybinding == ord('t'):
        speak("Attendence marked successfully")
        if present:
            with open("attendence/attendence_ +" + str(date) + '.csv', "+a") as csvfile:
                writer = csv.writer(csvfile)
                
                writer.writerow(attendence)
            csvfile.close()
            break
        else:
            with open("attendence/attendence_ +" + str(date) +'.csv', "+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(colNames)
                writer.writerow(attendence)
            csvfile.close()
            break

    if keybinding == ord("k"):
        speak("sayonara")
        break
output.release()
cv2.destroyAllWindows()
