# Invariant-Object-Tracking-System

This project demonstrates a robust object tracking system capable of tracking a specific face or rectangular object, remaining invariant to motion and rotation. The system combines real-time tracking capabilities and precision tracking methods with invariance through homographies.

# Features
	•	Real-Time Tracking: Utilizes optical flow and homography to track objects dynamically and account for rotation and motion invariance.
	•	Precise Tracking: Implements Meta’s CoTracker deep learning model for enhanced tracking accuracy.
	•	Motion & Rotation Invariance: Ensures consistent tracking performance even under challenging motion scenarios.

 Live Demos
	1.	Real-Time Tracking Video
A video showcasing the system’s live tracking capabilities, utilizing optical flow



https://github.com/user-attachments/assets/b228447a-0ab0-4551-9001-19539a165d5b


	2.	Precision Tracking Video
A video demonstrating the precision tracking system using CoTracker
Watch Precision Tracking Video

https://github.com/user-attachments/assets/9cdb41dc-54bc-463d-bf70-267c52a1a755



How It Works

1. Real-Time Tracking with Optical Flow
	•	Tracks object motion frame by frame using the Lucas-Kanade optical flow algorithm.
	•	Employs homography transformations to maintain invariance to rotation and scale changes.

2. Precision Tracking with CoTracker
	•	Integrates Meta’s CoTracker deep learning model for precise object localization.
	•	Also employs homography transformations to maintain invariance to rotation and scale changes.

3. Object Selection
	•	Allows users to select object to track from the initial frame (e.g. rectangular object).


