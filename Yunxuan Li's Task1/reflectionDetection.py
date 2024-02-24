import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Load data from the pickle file
with open('D:\gears_ncsu\Task.pickle', 'rb') as fh:
    data = pickle.load(fh)
    radar_cube = data['radar_cube']  # Get radar cube data

# Process radar data
radar_data_mag = np.abs(radar_cube).mean(axis=0).mean(axis=0)  # Compute average magnitude along both axes

# Find peaks in the radar data
peaks = find_peaks(radar_data_mag)[0] # Adjust distance parameter as needed

# print the magnitude and the peaks
print("Radar data magnitude information:", radar_data_mag)
print("Indices of found peaks:", peaks)


# Plot radar data magnitude
plt.figure(figsize=(10, 5))
plt.plot(radar_data_mag, label='Radar Data Magnitude')

# Plot peaks
plt.plot(peaks, radar_data_mag[peaks], 'x', color='red', label='Peaks')

# Add labels and title
plt.xlabel('Index')
plt.ylabel('Magnitude')
plt.title('Radar Data Magnitude and Peaks')
plt.legend()

# Show plot
plt.show()

