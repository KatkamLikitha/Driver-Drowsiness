# Driver Drowsiness Detection System

## Overview
This project detects driver drowsiness in real-time using computer vision and facial landmarks.
It monitors the driver’s eyes and mouth to identify signs of fatigue, and triggers an alarm if drowsiness is detected.

## Features
- Eye Aspect Ratio (EAR) for detecting closed eyes
- Mouth Aspect Ratio (MAR) for detecting yawning
- Real-time video stream processing using OpenCV
- Alarm system using pygame

## Setup Instructions
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Download the **dlib face landmarks model**:
   - [Download here](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
   - Extract and place `shape_predictor_68_face_landmarks.dat` inside the project folder.

3. Run the project:
   ```bash
   python main.py
   ```

4. Press `Q` to exit the program.

## Files
- `main.py` → Main detection script
- `alarm.wav` → Alarm sound file
- `requirements.txt` → Dependencies list
- `README.md` → Documentation

