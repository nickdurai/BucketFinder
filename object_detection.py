from ultralytics import YOLO
import cv2

def detect_objects(video_path):
    model = YOLO("yolov8n.pt")  # Load YOLO model
    results = model.predict(video_path, conf=0.2)  # Lower confidence for better detection

    ball_position = None
    hoop_position = None

    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls)  # Class ID
            label = model.names[cls_id]  # Class label (e.g., "sports ball", "person", etc.)

            print(f"Detected: {label} at {box.xyxy[0]}")  # Debugging

            # **Basketball detection (YOLO class 32: sports ball)**
            if cls_id == 32:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                ball_position = ((x1 + x2) // 2, (y1 + y2) // 2)

            # **Hoop detection (Trying multiple possible classes)**
            if cls_id in [0, 1, 2, 67]:  # Potential classes for hoop
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                hoop_position = ((x1 + x2) // 2, (y1 + y2) // 2)

    # **Debugging: Show detections**
    if not ball_position:
        print("⚠️ Basketball not detected!")
    if not hoop_position:
        print("⚠️ Hoop not detected!")

    return ball_position, hoop_position

if __name__ == "__main__":
    video_path = "C:/Users/nickd/Videos/Untitled video - Made with Clipchamp.mp4"
    ball, hoop = detect_objects(video_path)
    print(f"Detected Ball: {ball}, Hoop: {hoop}")
