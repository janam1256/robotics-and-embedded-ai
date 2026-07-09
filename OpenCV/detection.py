from ultralytics import YOLO
import cv2

# Load model
model = YOLO("runs/detect/train/weights/best.pt")

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    # Loop through every detected object
    for box in results[0].boxes:

        # Get coordinates
        x1, y1, x2, y2 = box.xyxy[0]

        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)

        # Confidence
        confidence = float(box.conf[0])

        # Ignore weak detections
        if confidence < 0.5:
            continue

        # Class ID
        class_id = int(box.cls[0])

        # Class Name
        class_name = model.names[class_id]

        # --------------------------
        # PERSON
        # --------------------------
        if class_name == "person":

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,0,255), 2)

            cv2.putText(frame,
                        "PERSON DETECTED",
                        (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0,0,255),
                        2)

            print("Person Detected")


        # --------------------------
        # BOTTLE
        # --------------------------
        elif class_name == "bottle":

            print("Bottle Found")

        # --------------------------
        # CHAIR
        # --------------------------
        elif class_name == "chair":

            cv2.rectangle(frame,
                          (x1,y1),
                          (x2,y2),
                          (0,255,0),
                          2)

        # --------------------------
        # CELL PHONE
        # --------------------------
        elif class_name == "cell phone":

            cv2.imwrite("phone_detected.jpg", frame)

            print("Phone Image Saved")

        # --------------------------
        # CAR
        # --------------------------
        elif class_name == "car":

            print("Playing Sound...")

    cv2.imshow("YOLO AI", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()