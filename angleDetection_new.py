import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
#TX1 -> RX1 TX1 -> RX4
#TX2 -> RX1 TX2 -> RX4
#TX3 -> RX1 TX3 -> RX4
azim_aoa_pairs = [[(0,0),(0,3)],[(1,0),(1,3)]]

#we have so many choices: like azim_aoa_pairs = [[(0,0),(0,3)],[(1,0),(1,3)],[(2,0),(2,3)]]


#TX1 -> RX1 TX2 -> RX1
#TX1 -> RX4 TX2 -> RX4
azim_aod_pairs = [[(0,0),(1,0)],[(0,3),(1,3)]]
# this is also the same thing

def cal_azim_aoa(radar_cube_single_bin):

    azim_aoas = []
    for(pair1, pair2) in azim_aoa_pairs:
        angle1 = np.angle(radar_cube_single_bin[pair1[0], pair1[1]])
        angle2 = np.angle(radar_cube_single_bin[pair2[0], pair2[1]])
        diff = np.angle(np.exp(1j*angle1)/np.exp(1j*angle2))
        angle = np.arcsin(diff/np.pi)
        azim_aoas.append(angle)

    azim_aoa = np.median(azim_aoas)
    return azim_aoa

def cal_azim_aod(radar_cube_single_bin):

    azim_aods = []
    for(pair1, pair2) in azim_aoa_pairs:
        angle1 = np.angle(radar_cube_single_bin[pair1[0], pair1[1]])
        angle2 = np.angle(radar_cube_single_bin[pair2[0], pair2[1]])
        diff = np.angle(np.exp(1j*angle1)/np.exp(1j*angle2))
        angle = np.arcsin(diff/(2*np.pi*1))
        azim_aods.append(angle)

    azim_aod = np.median(azim_aods)
    return azim_aod


def get_angles(radar_cube,peaks):

    angles = {}

    for peak in peaks:

        radar_cube_single_bin = radar_cube[..., peak]
        azim_aoa = np.degrees(cal_azim_aoa(radar_cube_single_bin))
        azim_aod = np.degrees(cal_azim_aod(radar_cube_single_bin))
        angles[peak] = (azim_aoa,azim_aod)

    return angles

with open(f'D:\gears_ncsu\Task.pickle', 'rb') as fh :
    # Load the data from the pickle file
    data = pickle.load(fh)

    # Access the loaded data
    radar_cube = data['radar_cube']  #

    radar_data_mag = np.abs(radar_cube).mean(axis=0).mean(axis=0)  

    peaks = find_peaks(radar_data_mag)[0]

    angles = get_angles(radar_cube,peaks)

    print(angles)




