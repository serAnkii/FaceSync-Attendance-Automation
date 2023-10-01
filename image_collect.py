import cv2
import pickle
import numpy
import os

output = cv2.VideoCapture(0)
faces = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")

faces_info = []
i = 0

name = input("enter your name: ")
while True:
    ok, frame = output.read()
    grayscalimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    facedata = faces.detectMultiScale(grayscalimg, 1.3, 5)  # threshold value

    # get coordinates
    for x, y, w, h in facedata:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)

        # : means all number of channels.
        cropped = frame[y : y + h, x : x + w, :]

        resize = cv2.resize(cropped, (40, 40))
        if len(faces_info) <= 100 and i % 10 == 0:
            faces_info.append(resize)
        i = i + 1
        cv2.putText(
            frame,
            str(len(faces_info)),
            (50, 50),
            cv2.FONT_HERSHEY_DUPLEX,
            2,
            (0, 0, 0),
            2,
        )
    cv2.imshow("window", frame)

    keybinding = cv2.waitKey(1)  # infinite time

    if keybinding == ord("k") or len(faces_info) >= 100:
        break
output.release()
cv2.destroyAllWindows()

# conver face data into a numpy array

faces_info = numpy.asarray(faces_info)

faces_info = faces_info.reshape(100, -1)

# store it inside a pickel file

# check for the presence of file and if present overwrite it

#name data
if "names.pkl" not in os.listdir("data/"):
    names = [name] * 100
    with open("data/names.pkl" , 'wb') as f:
        pickle.dump(names, f)
else:
    with open("data/names.pkl" , 'rb') as f:
        names = pickle.load(f)
    names = names + [name] * 100
    with open("data/names.pkl" , 'wb') as f:
        pickle.dump(names, f)

#face data

if "faces_dataset.pkl" not in os.listdir("data/"):
    with open("data/faces_dataset.pkl" ,"wb") as f:
        pickle.dump(faces_info, f)
else:
    with open("data/faces_dataset.pkl" , "rb") as f:
        pickelfaces = pickle.load(f)
    pickelfaces = numpy.append(pickelfaces,faces_info,axis=0)
    with open("data/faces_dataset.pkl" , 'wb') as f:
        pickle.dump(pickelfaces, f)

