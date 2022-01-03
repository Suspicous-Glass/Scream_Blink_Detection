import cv2
from playsound import playsound
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

def audio():
    playsound('scream.mp3')

first_read = True

cap = cv2.VideoCapture(0)
ret, image = cap.read()

while ret:
    ret, image = cap.read()
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_scale = cv2.bilateralFilter(gray_scale, 5, 1, 1)
    faces = face_cascade.detectMultiScale(gray_scale, 1.3, 5, minSize=(200, 200))
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            eye_face = gray_scale[y:y + h, x:x + w]
            eye_face_clr = image[y:y + h, x:x + w]
            eyes = eyes_cascade.detectMultiScale(eye_face, 1.3, 5, minSize=(50, 50))
            if len(eyes) >= 2:
                if first_read:
                    cv2.putText(image, "Eye's detected, press s to check blink", (70, 70), cv2.FONT_HERSHEY_SIMPLEX,
                                1, (0, 255, 0), 2)
                else:
                    cv2.putText(image, "Eye's Open", (70, 70), cv2.FONT_HERSHEY_SIMPLEX,
                                1, (255, 255, 255), 2)
            else:
                if first_read:
                    cv2.putText(image, "No Eye's detected", (70, 70), cv2.FONT_HERSHEY_SIMPLEX,
                                1, (255, 255, 255), 2)
                else:
                    cv2.putText(image, "Blink Detected.....!!!!", (70, 70), cv2.FONT_HERSHEY_SIMPLEX,
                                1, (0, 255, 0), 2)
                    cv2.imshow('image',image)
                    cv2.waitKey(1)
                    print("Blink Detected.....!!!!")
                    playsound('scream.mp3')
    else:
        cv2.putText(image, "No Face Detected.", (70, 70), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)
    cv2.imshow('image', image)
    a = cv2.waitKey(1)
    if a == ord('q'):
        break
    elif a == ord('s'):
        first_read = False
cap.release()
cv2.destroyAllWindows()