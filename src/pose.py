import cv2
import mediapipe as mp
import math
import sys

REFERENCE_CM = 160  # Wall black strip height

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
pose = mp_pose.Pose()

video_source = sys.argv[1] if len(sys.argv) > 1 else 0
cap = cv2.VideoCapture(video_source)

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb)

    if result.pose_landmarks:
        lm = result.pose_landmarks.landmark

        head = (int(lm[mp_pose.PoseLandmark.NOSE].x * w),
                int(lm[mp_pose.PoseLandmark.NOSE].y * h))

        ankle = (int(lm[mp_pose.PoseLandmark.LEFT_ANKLE].x * w),
                 int(lm[mp_pose.PoseLandmark.LEFT_ANKLE].y * h))

        shoulder_l = (int(lm[mp_pose.PoseLandmark.LEFT_SHOULDER].x * w),
                      int(lm[mp_pose.PoseLandmark.LEFT_SHOULDER].y * h))
        shoulder_r = (int(lm[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * w),
                      int(lm[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * h))

        elbow = (int(lm[mp_pose.PoseLandmark.LEFT_ELBOW].x * w),
                 int(lm[mp_pose.PoseLandmark.LEFT_ELBOW].y * h))

        wrist = (int(lm[mp_pose.PoseLandmark.LEFT_WRIST].x * w),
                 int(lm[mp_pose.PoseLandmark.LEFT_WRIST].y * h))

        ref_px = dist(ankle, wrist)  # ankle → wall mark (wrist touching strip)

        if ref_px > 30:
            px_per_cm = ref_px / REFERENCE_CM

            height_cm = dist(head, ankle) / px_per_cm
            shoulder_width_cm = dist(shoulder_l, shoulder_r) / px_per_cm
            arm_len_cm = (dist(shoulder_l, elbow) + dist(elbow, wrist)) / px_per_cm
            elbow_height_cm = dist(head, elbow) / px_per_cm

            cv2.putText(frame, f"Height: {int(height_cm)} cm", (20,40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
            cv2.putText(frame, f"Shoulder Width: {int(shoulder_width_cm)} cm", (20,75),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
            cv2.putText(frame, f"Arm Length: {int(arm_len_cm)} cm", (20,110),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
            cv2.putText(frame, f"Elbow Height: {int(elbow_height_cm)} cm", (20,145),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
        else:
            cv2.putText(frame, "Touch 160cm wall strip with LEFT WRIST",
                        (20,40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

        mp_draw.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.imshow("Ergonomic Measurement AI", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
