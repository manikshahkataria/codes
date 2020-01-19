import cv2, time
# 1 create object for external camera
vedio=cv2.VideoCapture(0)
a=0
while True:
    a=a+1
    #3 create a frame object
    check, frame=vedio.read()
    print(check)
    print(frame)
    #6 covert into grayscale
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 4show frame
    cv2.imshow("Capturing",gray)
    # 5 key to cut stop cpaturing
    key=cv2.waitKey(0)#stop capture
    if key  == ord('q'):
        break
print(a)

#2 shut down camera
vedio.release()