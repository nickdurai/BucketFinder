import cv2
import numpy as np

def auto_rotate_to_portrait(video_path, output_path):
    cap = cv2.VideoCapture(video_path)

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # If the video is already portrait, keep it as is
    if height > width:
        print("✅ Video is already in portrait mode. No rotation needed.")
        cap.release()
        return video_path  # Return the same path

    # Create output writer for rotated video
    out = cv2.VideoWriter(output_path, fourcc, fps, (height, width))  # Swap width & height

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Rotate frame to portrait mode (90° counterclockwise)
        rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
        out.write(rotated_frame)

    cap.release()
    out.release()
    print(f"✅ Video rotated to portrait and saved to {output_path}")

    return output_path  # Return the new file path

if __name__ == "__main__":
    input_video = "data/basketball_game.mp4"
    output_video = "data/basketball_game_portrait.mp4"

    auto_rotate_to_portrait(input_video, output_video)
