# 🧍 AI-Based Ergonomic Body Measurement

> Turn a normal laptop webcam into a contactless human body measurement tool.

## 🚀 Overview

Traditional body measurements using measuring tapes and stadiometers are slow, manual, and prone to human error.

This project uses **Computer Vision + AI Pose Estimation** to detect body landmarks through a webcam and estimate real-world body dimensions in centimeters.

The system uses a **160 cm reference calibration** to convert pixel distances into real-world measurements.

## ✨ What It Measures

- 📏 Body Height
- ↔️ Shoulder Width
- 💪 Arm Length
- 📐 Elbow Height

**Prototype accuracy:** approximately **±1–2 cm** under the tested controlled setup.

## ⚙️ How It Works

```text
Webcam
   ↓
Pose Detection
   ↓
MediaPipe Pose
   ↓
33 Body Landmarks
   ↓
Pixel → cm Calibration
   ↓
Real-Time Measurements
🛠️ Tech Stack

Python · OpenCV · MediaPipe Pose · Computer Vision

🌍 Applications
🛒 E-Commerce

Incorrect clothing sizes can lead to customer dissatisfaction and size-related returns. Camera-based body measurements could help platforms such as Amazon and Myntra improve size recommendations.

🏭 Industrial Ergonomics

Measure anthropometric dimensions for workstation, tool and equipment design.

🏥 Healthcare

Potential use in remote anthropometric assessment and clinical measurements.

👕 Tailoring & Apparel

Generate body measurements without conventional measuring tapes.

🎯 Future Scope
📱 Mobile application
🛍️ E-commerce size recommendations
🧍 3D body measurement
🦺 RULA/REBA-based ergonomic assessment
📊 Automated measurement reports
🎥 Dynamic posture analysis
📂 Project Structure
src/
├── pose.py
└── launcher.py

media/
demo/
docs/
▶️ Run the Project
pip install -r requirements.txt
python src/launcher.py

A webcam and suitable calibration setup are required.
