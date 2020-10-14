#TASK 4 RESPONSES

#PART 1: HSV is typically better than RGB for the purposes of this trial because it is easier to represent a wide range of hues and tinges for a single color.
#PART 2: When changing the lighting conditions, I found that too much light produced a glare off of the object, similarly, lighting that was too dim did not reflect enough color back to the camera. This resulted in less consistent recognition of that color from my webcam
#PART 3: Changing phone brightness of the camera helped with the recognition of color. This is likely due to the webcam focusing/altering its aperture to the brightness of a very intense screen/light.



import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    frame = cap.read()
    frame=frame[1]

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([230,50,50])
    upper_blue = np.array([255,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()