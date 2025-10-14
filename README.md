# Attendance-System

//This is For the head count based setup 

# Face Recognition Attendance System

This project detects faces using a camera and counts the number of people present. It records the maximum count in a CSV file as attendance.

---

## Requirements

- Python 3.8 or higher
- A working webcam

---

## Setup Steps

### 1. Download or Copy the Project
Copy the project folder to your computer.

---

### 2. Open the Project
Open the folder in VS Code or any code editor.

---

### 3. Create a Virtual Environment
Open a terminal in the project folder and run:

python -m venv venv

yaml


Activate it:

- For Windows:
venv\Scripts\activate

diff


---

### 4. Install Required Packages
Run this command in the terminal:

pip install -r requirements.txt

go


If you don’t have `requirements.txt`, you can install manually:

pip install opencv-python mediapipe pyttsx3

yaml


---

### 5. Run the Program
Run this command:

python camera_recognition.py

yaml


---

### 6. How It Works
- The camera opens for 15 seconds.
- It counts how many faces are detected.
- When finished, the result is saved in `attendance_log.csv`.

---

### 7. Stop the Program
Press `Q` to stop it anytime.

---

### 8. Check Results
After it finishes, open `attendance_log.csv` to see the date, time, and number of people detected.

---

### 9. Notes
- Make sure your webcam is working.
- Do not run any other app that uses the camera.
- If any library error appears, reinstall the missing package using pip.

---

### Example Output
Timestamp,Duration(sec),MaxPeople
2025-10-14 18:30:00,15,2
