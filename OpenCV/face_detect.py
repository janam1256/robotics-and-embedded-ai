import cv2
import time

# Load face detection model
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Start camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera not accessible")
    exit()

last_saved_time = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Display face count
    text = f"Faces: {len(faces)}"
    cv2.putText(frame, text, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # If face detected → save image (every 3 seconds max)
    if len(faces) > 0:
        current_time = time.time()

        if current_time - last_saved_time > 3:
            filename = f"face_{int(current_time)}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Saved: {filename}")
            last_saved_time = current_time

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Face Detection System', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        print("Exiting...")
        break

cap.release()
cv2.destroyAllWindows()



