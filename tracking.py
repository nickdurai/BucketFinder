import cv2
import numpy as np
from score_detection import detect_score

def initialize_kalman():
    kf = cv2.KalmanFilter(4, 2)  # 4 state variables (x, y, dx, dy), 2 measurements (x, y)
    kf.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], np.float32)
    kf.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)
    kf.processNoiseCov = np.eye(4, dtype=np.float32) * 0.03  # Noise filter
    return kf

def track_ball(video_path, initial_position, hoop_position):
    cap = cv2.VideoCapture(video_path)
    kalman = initialize_kalman()
    trajectory = {}  # Stores ball positions per frame
    frame_number = 0

    measurement = np.array([[np.float32(initial_position[0])], [np.float32(initial_position[1])]])
    kalman.correct(measurement)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_number += 1
        prediction = kalman.predict()
        predicted_x, predicted_y = int(prediction[0]), int(prediction[1])

        # **Store ball position for scoring analysis**
        trajectory[frame_number] = (predicted_x, predicted_y)

        # **Draw tracking visualization**
        cv2.circle(frame, (predicted_x, predicted_y), 10, (0, 255, 0), -1)  # Green ball tracking
        cv2.imshow("Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # **Step 4: Detect scores from trajectory**
    scoring_frames = detect_score(trajectory, hoop_position)
    return scoring_frames  # Return frames where a score was detected

if __name__ == "__main__":
    from object_detection import detect_objects

    video_path = "data/basketball_game.mp4"
    ball_position, hoop_position = detect_objects(video_path)

    if ball_position and hoop_position:
        print(f"Ball: {ball_position}, Hoop: {hoop_position}")
        score_frames = track_ball(video_path, ball_position, hoop_position)
        print(f"🏀 Scoring detected at frames: {score_frames}")
    else:
        print("⚠️ Ball or hoop not detected.")
