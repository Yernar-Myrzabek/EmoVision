# EmotionSentiment-AI

A lightweight, real-time emotion recognition system built with Python and OpenCV. 

## Overview
This project explores **Heuristic-based Computer Vision**. Instead of relying on heavy, "black-box" neural networks, this system uses **Haar Cascade classifiers** to identify facial features and applies custom geometric logic to classify emotional states (Happy, Angry, Sad, Neutral) in real-time.

## Tech Stack
- **Language:** Python 3.11
- **Computer Vision:** OpenCV (Open Source Computer Vision Library)
- **Architecture:** Modular MVC (Model-View-Controller) pattern

## How it Works
1. **Frame Acquisition:** Captures live video stream from the webcam.
2. **Preprocessing:** Converts frames to grayscale to optimize contrast analysis.
3. **Feature Extraction:** Uses ROI (Region of Interest) mapping to locate the face, eyes, and mouth.
4. **Logic:** Applies a rule-based algorithm to determine emotion based on detected facial features.
5. **UI Rendering:** Overlays a custom Cyber-HUD (Heads-Up Display) onto the video feed.

## ⚙️Installation
1. Clone this repository:
   `git clone https://github.com/Yernar-Myrzabek/EmoVision`
2. Install the required dependencies:
   `pip install -r requirements.txt`
3. Run the application:
   `python main.py`
4.  "Optimized for Apple Silicon (M3). Runs at high FPS using native OpenCV hardware acceleration."

## Future Work
Future iterations will focus on transitioning from heuristic rules to **Support Vector Machines (SVM)** to increase detection accuracy.
