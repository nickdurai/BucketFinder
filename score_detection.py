import numpy as np

def detect_score(trajectory, hoop_position, frame_rate=30):
    """
    Detects when a score occurs based on ball movement.
    :param trajectory: Dictionary {frame_number: (x, y)} storing ball positions
    :param hoop_position: (x, y) coordinates of the hoop center
    :param frame_rate: FPS of the video (used to calculate time-based movement)
    :return: List of frames where a score is detected
    """

    scoring_frames = []
    scoring_zone_top = hoop_position[1] + 20  # Define scoring zone just below hoop
    scoring_zone_bottom = hoop_position[1] + 80  # Adjust based on hoop height

    last_y = None  # Previous frame's ball position
    falling_speed = []  # Stores ball velocity changes

    for frame, (x, y) in trajectory.items():
        # **Step 1: Check if ball enters the scoring zone**
        if scoring_zone_top <= y <= scoring_zone_bottom:
            # **Step 2: Track ball velocity (falling speed)**
            if last_y is not None:
                velocity = y - last_y  # Positive if ball is falling
                falling_speed.append(velocity)

            # **Step 3: If ball disappears quickly, count as score**
            if len(falling_speed) > 5:  # Check last 5 frames
                avg_speed = np.mean(falling_speed[-5:])
                if avg_speed > 10:  # If ball is falling fast
                    scoring_frames.append(frame)

        last_y = y  # Store last frame's Y position

    return scoring_frames  # Return frames where a score was detected
