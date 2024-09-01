import pandas as pd

def get_frame_idx_for_n(df, n_value):
    # Filter the DataFrame where 'n' equals 'n_value'
    result = df[df['n'] == n_value]

    # Check if any row matches the condition
    if not result.empty:
        # Get the value of 'frame_idx' for the matched row
        frame_idx = result.iloc[0]['frame_idx']
        return frame_idx
    else:
        return None  # Return None if no matching row is found


# Example usage:
# Assuming you have a DataFrame 'df' with the columns ['n', 'pts_time', 'fps', 'frame_idx']
n_value = 10  # Replace with your specific 'n_value'
frame_idx = get_frame_idx_for_n(df, n_value)

if frame_idx is not None:
    print(f"Frame index for n = {n_value}: {frame_idx}")
else:
    print(f"No matching row found for n = {n_value}")
