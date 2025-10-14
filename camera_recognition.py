import cv2
import time
import csv
import os
import pyttsx3
from datetime import datetime
import mediapipe as mp   


CAMERA_SOURCE = 0
DURATION = 15
CSV_FILE = "attendance_log.csv"


cap = cv2.VideoCapture(CAMERA_SOURCE)
if not cap.isOpened():
    print("❌ Could not open camera")
    exit()

engine = pyttsx3.init()
mp_face = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.6)

start_time = time.time()
max_count = 0

print(f"🎥 Starting headcount for {DURATION} seconds...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_face.process(rgb)

    count = 0
    if results.detections:
        for detection in results.detections:
            count += 1
            bboxC = detection.location_data.relative_bounding_box
            h, w, c = frame.shape
            x, y, w_box, h_box = int(bboxC.xmin * w), int(bboxC.ymin * h), \
                                 int(bboxC.width * w), int(bboxC.height * h)
            cv2.rectangle(frame, (x, y), (x + w_box, y + h_box), (0, 255, 0), 2)

    max_count = max(max_count, count)

    cv2.putText(frame, f"People: {count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("Attendance Headcount", frame)

    if time.time() - start_time > DURATION:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
header = ["Timestamp", "Duration(sec)", "MaxPeople"]

row = [timestamp, DURATION, max_count]

file_exists = os.path.isfile(CSV_FILE)
with open(CSV_FILE, mode="a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(header)
    writer.writerow(row)

print(f"✅ Attendance log saved in {CSV_FILE}")
print(f"👥 Max {max_count} people detected")


engine.say(f"{max_count} people detected")
engine.runAndWait()
