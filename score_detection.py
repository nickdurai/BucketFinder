def detect_score(trajectory, hoop_position):
    for frame, pos in trajectory.items():
        if pos[1] > hoop_position[1]:  # If ball goes below hoop
            print(f"Basket scored at frame {frame}")
            return frame
