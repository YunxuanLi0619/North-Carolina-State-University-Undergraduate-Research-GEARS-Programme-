import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
with open(f'D:\gears_ncsu\Task.pickle', 'rb') as fh :
    # Load the data from the pickle file
    data = pickle.load(fh)

    # Access the loaded data
    radar_cube = data['radar_cube']  ## This radar cube has info of all the 12 antennas

    # Take average across both the axii (Tx and Rx) and then plot the average
    range_data_mag = np.abs(radar_cube).mean(axis=0).mean(axis=0)
    plt.plot(range_data_mag)
    plt.xlabel('Distance: 1 bin = 3.75cm')
    plt.ylabel('Amplitude')
    plt.show()
    plt.draw()



# To plot for (TX,RX) (0,0), (1,1) ...
with open(f'D:\gears_ncsu\Task.pickle', 'rb') as fh :
    radar_cube = pickle.load(fh)
    radar_cube = radar_cube['radar_cube']
    radar_cube1 = radar_cube[0][0]
    avg = radar_cube1/radar_cube1.max()
    radar_cube2 = radar_cube[1][1]
    avg_ = radar_cube2/radar_cube2.max()
    plt.xlabel('Distance: 1 bin = 3.75cm')
    plt.ylabel('Amplitude')
    
    plt.plot(np.abs(avg))
    plt.plot(np.abs(avg_))
    plt.show()

