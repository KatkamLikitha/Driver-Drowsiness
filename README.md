# Driver Drowsiness Detection System

## Project Overview
The **Driver Drowsiness Detection System** is an AI-powered application designed to monitor a driver's alertness in real-time. It detects **eye closure and fatigue** using computer vision techniques and alerts the driver to prevent accidents caused by drowsiness.

---

## Features
- Real-time detection of closed and open eyes using webcam or video feed  
- Alert system (audio or visual) when drowsiness is detected  
- Frame-by-frame analysis of eye aspect ratio  
- Logging of drowsiness events for further analysis  
- Lightweight and can run on standard laptops  

---

## Technologies Used
- **Programming Language:** Python  
- **Computer Vision:** OpenCV, Dlib, MediaPipe (optional)  
- **Machine Learning:** Eye aspect ratio (EAR) calculation or CNN models  
- **Audio Alerts:** playsound or simple beep for alerts  
- **Data Handling:** NumPy, Pandas (optional for logging)  

---

## Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd Driver_Drowsiness_Detection
Create virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Run the application

python drowsiness_detection.py

How it Works

The webcam captures real-time video of the driver’s face.

The system detects facial landmarks, focusing on eyes.

Eye Aspect Ratio (EAR) is calculated to determine if eyes are closed.

If the EAR drops below a threshold for a certain number of frames, the system triggers an alert.

Optionally, drowsiness events can be logged for further analysis.

Folder Structure
Driver_Drowsiness_Detection/
│
├── README.md
├── requirements.txt
├── drowsiness_detection.py  # Main detection script
├── haarcascade/             # Optional: Haar cascade files for face/eye detection
├── utils/
│   └── alarm.py             # Alert system (sound or beep)
├── data/                    # Optional: test videos or images
└── docs/
    └── Project_Documentation.pdf

Dependencies

OpenCV

Dlib

NumPy

imutils

playsound (for audio alerts)

Usage

Connect your webcam

Run drowsiness_detection.py

The system will monitor eyes and trigger alerts if drowsiness is detected

Future Enhancements

Integrate deep learning model (CNN) for more accurate eye closure detection

Support mobile devices or embedded systems (e.g., Raspberry Pi)

Add dashboard for monitoring driver statistics

Implement SMS or notification alerts in case of prolonged drowsiness
