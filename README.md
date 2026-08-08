# 🧍 AI-Based Ergonomic Body Measurement

> A computer vision system that uses a laptop webcam to measure human body dimensions in real time.

## 🚀 Overview

The system uses **Python, OpenCV and MediaPipe Pose** to detect human body landmarks and convert pixel measurements into real-world dimensions using a **160 cm reference calibration**.

## ✨ Measurements

- 📏 Body Height
- ↔️ Shoulder Width
- 💪 Arm Length
- 📐 Elbow Height

**Prototype accuracy:** approximately **±1–2 cm** under the tested controlled setup.

## ⚙️ How It Works

Webcam → MediaPipe Pose → 33 Body Landmarks → Pixel-to-cm Calibration → Real-Time Measurements

## 🛠️ Tech Stack

**Python · OpenCV · MediaPipe Pose · Computer Vision**

## 🎯 Future Scope

- 📱 Mobile application
- 🛍️ E-commerce size recommendations
- 🧍 3D body measurement
- 🦺 RULA/REBA-based ergonomic assessment
- 📊 Automated measurement reports
- 🎥 Dynamic posture analysis

## ▶️ Run

```bash
pip install -r requirements.txt
python src/launcher.py
```
A webcam and suitable calibration setup are required.
