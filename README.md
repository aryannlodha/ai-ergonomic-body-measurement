# AI-Based Ergonomic Measurement of Human Body

> A low-cost, contactless computer-vision system that uses a laptop webcam to estimate key human body dimensions in real time.

## Overview

This project demonstrates an AI-based ergonomic measurement system developed for the **Work System Design / Project Based Learning** context at RV College of Engineering.

The system uses a standard laptop camera to capture a live video stream, detects human body landmarks using **MediaPipe Pose**, processes the frames with **OpenCV**, and converts pixel distances into real-world measurements using a fixed **160 cm reference**.

The prototype focuses on:

- Total body height
- Shoulder width
- Arm length
- Elbow height

The project is designed around a controlled single-camera setup and static standing posture.

## Problem Statement

Traditional ergonomic and anthropometric measurements commonly rely on measuring tapes, anthropometers, and stadiometers. These approaches can be time-consuming, contact-based, dependent on manual measurement, and difficult to scale.

This project explores whether a normal webcam can be turned into a practical digital measurement instrument.

## Objectives

- Develop an AI-based system for ergonomic body measurement.
- Reduce dependence on manual measuring tools.
- Convert pixel measurements into centimetres using real-world calibration.
- Display ergonomic dimensions in real time.
- Explore applications in workstation design, e-commerce sizing, healthcare, and digital ergonomics.

## How It Works

```text
Laptop Webcam
      ↓
Live Video Frames
      ↓
MediaPipe Pose
      ↓
Body Landmark Detection
      ↓
Pixel-Distance Calculation
      ↓
160 cm Reference Calibration
      ↓
Pixel → Centimetre Conversion
      ↓
Real-Time Measurements
```

### Calibration

The experimental setup uses a fixed **160 cm reference strip**. The subject stands at a fixed floor position and touches the reference using the left wrist.

The project report defines the scale as:

```text
pixels_per_cm = pixel_distance(ankle → wrist) / 160
```

The calculated scale is then applied to the other pixel distances.

## Measurements

The prototype computes measurements from relevant body landmarks using Euclidean distance.

| Measurement | Landmark basis |
|---|---|
| Total body height | Head → ankle |
| Shoulder width | Left shoulder → right shoulder |
| Arm length | Shoulder → elbow → wrist |
| Elbow height | Head → elbow |

## Experimental Setup

The documented setup uses:

- Laptop webcam
- Camera approximately 3 m from the subject
- Camera aligned approximately perpendicular to the subject
- 160 cm wall reference
- Fixed floor mark
- Adequate indoor lighting
- Upright standing posture

## Technology Stack

| Category | Technology |
|---|---|
| Language | Python |
| Pose estimation | MediaPipe Pose |
| Computer vision | OpenCV |
| Camera | Laptop webcam |
| Measurement | Euclidean geometry + calibration |
| Output | Real-time on-screen visualization |

## Reported Results

According to the project documentation, the prototype successfully produced real-time body measurements using a laptop camera.

The project reports approximately **±1–2 cm accuracy** under the controlled experimental setup. Minor variation was observed due to posture and lighting.

## Limitations

The current methodology assumes:

- Static standing posture
- Fixed camera distance and alignment
- Adequate lighting
- A known reference dimension
- A single-camera setup

The current prototype should therefore be treated as a controlled proof-of-concept rather than a general-purpose anthropometric measurement system.

## Future Scope

Potential extensions documented for the project include:

- RULA and REBA-based ergonomic risk assessment
- Multi-camera or depth-camera measurement
- Dynamic posture and movement analysis
- Automatic report generation
- Data storage and dashboards
- Workstation optimization
- Furniture and tool ergonomics
- E-commerce size recommendation
- Mobile application
- 3D body scanning

## Repository Structure

```text
AI-Based-Ergonomic-Measurement/
├── src/                    # Project source code
├── docs/                   # Report, presentation and poster
├── media/                  # Methodology, workflow and result images
├── demo/                   # Demonstration media, when applicable
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Documentation

The `docs/` folder contains the academic project documentation and presentation material.

## Authors

**Aryan Lodha**  
RV College of Engineering  
Industrial Engineering and Management

**Harsh Jain**  
RV College of Engineering  
Industrial Engineering and Management

## Academic Context

Work System Design / Project Based Learning  
RV College of Engineering, Bengaluru

## References

The project documentation references work on:

- MediaPipe / BlazePose
- OpenCV
- Human pose estimation
- Camera calibration
- Anthropometry and ergonomics
- ISO 7250-1
- RULA and REBA

See the project report in `docs/` for the full reference list.

## Disclaimer

This repository documents an academic prototype. Measurement accuracy depends on camera position, calibration, posture, lighting, landmark detection and other experimental conditions.
