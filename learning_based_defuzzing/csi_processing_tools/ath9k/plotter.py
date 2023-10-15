import time

import matplotlib.pyplot as plt
import numpy as np

interval = 0.01

def plot_single(csi_array, no_subcarriers, filename):
    fig, axs = plt.subplots(2)
    fig.suptitle('Ath9K CSI Plotter - ' + filename)
    x_amp = np.arange(0, no_subcarriers)
    x_pha = np.arange(0, no_subcarriers)
    axs[0].plot(x_amp, np.abs(csi_array))
    axs[1].plot(x_pha, np.angle(csi_array,deg=False))
    plt.pause(interval/10)
    time.sleep(interval)


def clear_plot(axs):
        axs[0].clear()
        axs[1].clear()
        axs[0].set_ylabel('Amplitude (dBm)')
        axs[1].set_ylabel('Phase (rad)')
        axs[1].set_xlabel('Subcarrier')
