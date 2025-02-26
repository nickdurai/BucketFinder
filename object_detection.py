from ultralytics import YOLO
import cv2

def detect_objects(video_path):
    model = YOLO("yolov8n.pt")  # Load YOLO model
    results = model.predict(video_path, conf=0.25)  # Lower confidence to catch more objects

    ball_position = None
    hoop_position = None

    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls)
            label = model.names[cls_id]  # Get object class label

            # Print detected objects for debugging
            print(f"🟡 Detected: {label} at {box.xyxy[0]}")

            if label == "sports ball":  # Class name instead of ID
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2
                ball_position = (center_x, center_y)

            elif label in ["goalpost", "basketball hoop"]:  # Try alternative hoop labels
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                hoop_position = (center_x, center_y)

    if ball_position is None:
        print("⚠️ No basketball detected!")

    if hoop_position is None:
        print("⚠️ No hoop detected!")

    return ball_position, hoop_position

if __name__ == "__main__":
    video_path = "data/basketball_game.mp4"
    ball, hoop = detect_objects(video_path)
    print(f"🎯 Final Detection -> Ball: {ball}, Hoop: {hoop}")
