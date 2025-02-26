import cv2

def extract_frames(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(f"{output_folder}/frame_{frame_count}.jpg", frame)
        frame_count += 1

    cap.release()
    print(f"Extracted {frame_count} frames.")

if __name__ == "__main__":
    extract_frames("data/basketball_game.mp4", "data/frames")
