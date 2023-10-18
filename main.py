import numpy as np
import matplotlib.pyplot as plt

# Simulate ECG data (replace with your own data)
# Typically, ECG data consists of time and voltage measurements.
# You can replace this example with your own data.
time = np.linspace(0, 10, 1000)  # Time in seconds
ecg_data = np.sin(2 * np.pi * 1 * time) + 0.5 * np.sin(2 * np.pi * 2 * time)

# Plot the ECG data
plt.figure(figsize=(10, 4))
plt.plot(time, ecg_data)
plt.title('ECG Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Analyze heart rate
# To analyze heart rate, you can use peak detection algorithms.
# One common method is the Pan-Tompkins algorithm.
# You may need to install additional libraries, e.g., scipy and biosppy,
# for more advanced heart rate analysis.

# Example peak detection
from scipy.signal import find_peaks

peaks, _ = find_peaks(ecg_data, height=0.5)  # Adjust the height threshold

# Calculate heart rate in beats per minute (BPM)
heart_rate = 60 / (np.diff(peaks).mean() / len(time))

print(f'Heart rate: {heart_rate:.2f} BPM')

# Plot ECG with detected peaks
plt.figure(figsize=(10, 4))
plt.plot(time, ecg_data, label='ECG Signal')
plt.plot(time[peaks], ecg_data[peaks], 'ro', label='Peak')
plt.title('ECG Signal with Peaks')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.show()
