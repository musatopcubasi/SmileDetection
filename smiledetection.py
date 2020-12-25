import cv2
from time import sleep

facecas=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smilecas=cv2.CascadeClassifier("haarcascade_smile.xml")

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    gray=cv2.erode(gray,None,iterations=2)
    gray=cv2.dilate(gray,None,iterations=2)

    try:
        yuzler=facecas.detectMultiScale(gray,1.1,3)#should be changed according to the environment
        for (x,y,w,h) in yuzler:
            smilearea=gray[y:y+h,x:x+w]

        smile = smilecas.detectMultiScale(smilearea, 1.3, 3)#should be changed according to the environment
        print(len(smile))

        if len(smile) ==0:#return error if smile isn't detect
            sleep(0.5)
            raise ValueError

        for (xs,ys,ws,hs) in smile:
            cv2.rectangle(frame,(x+xs,y+ys),(x+xs+ws,y+ys+hs),(255,255,0),3)
            cv2.rectangle(smilearea,(xs,ys),(xs+ws,ys+hs),(255,255,0),3)

        cv2.imshow("smile area", smilearea)
        cv2.imshow("frame", frame)

    except:
        print("Will retry after 1 seconds")
        sleep(1)

    if cv2.waitKey(25) and 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()