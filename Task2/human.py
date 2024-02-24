import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


def max_peak(peaks, range_data_mag):
    temp = []

    for i in range(len(peaks[0])):
        temp.append(range_data_mag[peaks[0][i]])
    temp = sorted(temp, reverse=True)
    max_result = np.where(range_data_mag == temp[0])[0][0]
    max_peak_second = np.where(range_data_mag == temp[1])[0][0]

    return max_result, max_peak_second


static_constant = 10
n_range_bins = 300
n_frames = n_range_bins - static_constant

with open(
        f'D:\gears_ncsu\human.pickle',
        'rb') as fh:
    # Load the data from the pickle file
    data = pickle.load(fh)

    # Access the loaded data
    radar_cube_list = data['radar_cube_list']
    maximumpeak = data['max_bin']
    mags_breathing = data['mags_breathing']
    phases_breathing = data['phases_breathing']
    subtracted_range_profile_average = data['bkg_subtracted']

    fft_mag = np.abs(np.fft.fft(mags_breathing[static_constant:]))
    fft_pha = np.abs(np.fft.fft(phases_breathing[static_constant:]))

    # Find peaks in fft_mag
    peaks_fft_mag = find_peaks(fft_mag)
    breath, heart = max_peak(peaks_fft_mag, fft_mag)
    print(fft_mag[breath], fft_mag[heart])
    print('Using Mag: ', fft_mag[breath] * 60, fft_mag[heart] * 60)

    # Find peaks in fft_pha
    # peaks_fft_pha = find_peaks(fft_pha)
    # breath_pha, heart_pha = max_peak(peaks_fft_pha, fft_pha)
    # print('Using pha: ', breath_pha * 60, heart_pha * 60)

    print(maximumpeak)
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 2, 1)
    plt.plot(mags_breathing[
             static_constant:])  ## this 10 is because we are finding fft after 10 frames because in first 10 frames subtracted profile is being calculated
    plt.xlabel('Mag')
    plt.subplot(2, 2, 3)
    plt.plot(np.unwrap(phases_breathing[static_constant:]))
    plt.xlabel('Phase')
    plt.subplot(2, 2, 2)
    xf = np.fft.rfftfreq(n_frames, 1 / 5)
    plt.plot(xf[2:], fft_mag[2:int(n_frames / 2 + 1)])
    plt.xlabel('Mag FFT')
    plt.subplot(2, 2, 4)
    plt.plot(xf[2:], fft_pha[2:int(n_frames / 2 + 1)])
    plt.xlabel('Pha FFT')
    plt.show()