import cv2

# Load Haar cascade for face (head) detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Open webcam (or replace 0 with video file path)
cap = cv2.VideoCapture(0)

# Create a CSRT tracker (no cv2.legacy needed in OpenCV 4.12+)
tracker = cv2.TrackerCSRT_create()
tracking = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for performance
    frame = cv2.resize(frame, (960, 540))

    if not tracking:
        # Detect faces (heads)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))

        for (x, y, w, h) in faces:
            # Initialize tracker with the first detected face
            tracker = cv2.TrackerCSRT_create()  # re-create tracker
            tracker.init(frame, (x, y, w, h))
            tracking = True
            break  # Track only the first detected head for now

    else:
        # Update tracker
        success, box = tracker.update(frame)
        if success:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "Tracking Head", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        else:
            tracking = False  # Lost tracking, re-detect

    cv2.imshow("Human Head Tracker", frame)

    key = cv2.waitKey(30) & 0xFF
    if key == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()