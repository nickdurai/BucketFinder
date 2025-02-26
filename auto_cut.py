import ffmpeg

def cut_video(input_video, start_time, end_time, output_video):
    (
        ffmpeg
        .input(input_video, ss=start_time, to=end_time)
        .output(output_video)
        .run()
    )

def create_highlights(video_path, scored_frames, fps=30):
    for i, frame in enumerate(scored_frames):
        start_time = max(0, (frame - (fps * 3)) / fps)  # 3 seconds before
        end_time = (frame + (fps * 3)) / fps  # 3 seconds after
        output_video = f"output/highlight_{i+1}.mp4"

        print(f"Saving highlight: {output_video} (Frames {frame-90} to {frame+90})")
        cut_video(video_path, start_time, end_time, output_video)

if __name__ == "__main__":
    scored_frames = [300, 750]  # Example frame numbers
    create_highlights("data/basketball_game.mp4", scored_frames)
