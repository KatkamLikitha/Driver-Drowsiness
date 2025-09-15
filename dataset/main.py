import cv2
import pygame
import time

# Initialize pygame mixer for alarm
pygame.mixer.init()
pygame.mixer.music.load("alarm.mp3")  # make sure alarm.wav is in the same folder

# Load Haarcascades (built into OpenCV)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# Open webcam
cap = cv2.VideoCapture(0)

# Counters
eye_closed_frames = 0
EYE_CLOSED_THRESHOLD = 20  # number of frames eyes must be closed to trigger alarm

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Detect eyes inside face ROI
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) == 0:
            eye_closed_frames += 1
        else:
            eye_closed_frames = 0

        # If eyes closed for too long → ALARM
        if eye_closed_frames > EYE_CLOSED_THRESHOLD:
            cv2.putText(frame, "DROWSINESS ALERT!", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()

    cv2.imshow("Driver Drowsiness Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()