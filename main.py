from video_processing import auto_rotate_to_portrait
from object_detection import detect_objects
from tracking import track_ball
from auto_cut import create_highlights

def main():
    input_video = "INSERT VIDEO DIRECTORY"
    portrait_video = "data/basketball_game_portrait.mp4"

    # Step 1: Ensure video is in portrait mode
    portrait_video = auto_rotate_to_portrait(input_video, portrait_video)

    # Step 2: Detect ball & hoop
    ball_position, hoop_position = detect_objects(portrait_video)

    if ball_position and hoop_position:
        print(f"Ball at {ball_position}, Hoop at {hoop_position}")

        # Step 3: Track the ball & detect scoring moments
        scored_frames = track_ball(portrait_video, ball_position, hoop_position)

        # Step 4: Cut highlights
        if scored_frames:
            create_highlights(portrait_video, scored_frames)
            print("🎥 Highlights saved successfully.")
        else:
            print("⚠️ No scores detected.")

    else:
        print("⚠️ Error: Ball or hoop not detected.")

if __name__ == "__main__":
    main()
