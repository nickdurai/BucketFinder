import ffmpeg
import os

# Set the output directory outside the project (change this to your preferred location)
OUTPUT_DIR = "C:/Videos/BucketFinder"  # Windows
# OUTPUT_DIR = "/Users/yourname/Videos/BucketFinder"  # macOS/Linux

# Ensure the directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def cut_video(input_video, start_time, end_time, output_filename):
    output_path = os.path.join(OUTPUT_DIR, output_filename)  # Save outside project
    (
        ffmpeg
        .input(input_video, ss=start_time, to=end_time)
        .output(output_path)
        .run()
    )
    print(f"✅ Highlight saved to: {output_path}")

def create_highlights(video_path, scored_frames, fps=30):
    for i, frame in enumerate(scored_frames):
        start_time = max(0, (frame - (fps * 3)) / fps)  # 3 seconds before
        end_time = (frame + (fps * 3)) / fps  # 3 seconds after
        output_filename = f"highlight_{i+1}.mp4"

        print(f"🎥 Saving highlight: {output_filename} (Frames {frame-90} to {frame+90})")
        cut_video(video_path, start_time, end_time, output_filename)

if __name__ == "__main__":
    scored_frames = [300, 750]  # Example frame numbers
    create_highlights("data/basketball_game.mp4", scored_frames)
