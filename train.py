from sklearn.neighbors import KNeighborsClassifier
import pickle
import numpy
import os
import cv2

output = cv2.VideoCapture(0)
faces = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")


with open("data/faces_dataset.pkl", "rb") as f:
    FACES = pickle.load(f)

with open("data/names.pkl", "rb") as f:
    LABLES = pickle.load(f)


knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(FACES,LABLES)

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

        cv2.putText(frame,str(oput[0]),(x,y-15),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(0,0,0),2)

    cv2.imshow("window", frame)

    keybinding = cv2.waitKey(1)  # infinite time

    if keybinding == ord("k"):
        break
output.release()
cv2.destroyAllWindows()
