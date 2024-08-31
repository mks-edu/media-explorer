import pandas as pd

# Specify the path to your CSV file
file_path = r"\Data_2024\Map Keyframe\map-keyframes-b1\map-keyframes\L01_V001.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df.head())
