from object_detection import detect_objects
from tracking import track_ball
from auto_cut import create_highlights

def main():
    video_path = "INSERT VIDEO DIRECTORY"

    # Step 1: Detect ball & hoop
    ball_position, hoop_position = detect_objects(video_path)

    if ball_position and hoop_position:
        print(f"Ball at {ball_position}, Hoop at {hoop_position}")

        # Step 2: Track the ball & detect scoring moments
        scored_frames = track_ball(video_path, ball_position, hoop_position)

        # Step 3: Cut highlights
        if scored_frames:
            create_highlights(video_path, scored_frames)
            print("Highlights saved successfully.")
        else:
            print("No scores detected.")

    else:
        print("Error: Ball or hoop not detected.")

if __name__ == "__main__":
    main()
