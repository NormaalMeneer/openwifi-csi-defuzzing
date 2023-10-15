from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def plot(csi, start = 0, end=-1 , title=""):
    if(end <= start):
        end = start+1
    for index in range(start,end):
        fig_csi = plt.figure()
        fig_csi.clf()
        ax_abs_csi = fig_csi.add_subplot(211)
        ax_abs_csi.set_xlabel("subcarrier idx")
        ax_abs_csi.set_ylabel("abs")
        ax_abs_csi.set_title("CSI " + title)
        plt.plot(np.abs(csi[index]))
        ax_phase_csi = fig_csi.add_subplot(212)
        ax_phase_csi.set_xlabel("subcarrier idx")
        ax_phase_csi.set_ylabel("phase")
        plt.plot(np.angle(csi[index]))
        plt.ion()
        plt.pause(0.005)

def plot_single(csi, title=""):
    fig_csi = plt.figure()
    fig_csi.clf()
    ax_abs_csi = fig_csi.add_subplot(211)
    ax_abs_csi.set_xlabel("subcarrier idx")
    ax_abs_csi.set_ylabel("abs")
    ax_abs_csi.set_title("CSI " + title)
    plt.plot(np.abs(csi))
    ax_phase_csi = fig_csi.add_subplot(212)
    ax_phase_csi.set_xlabel("subcarrier idx")
    ax_phase_csi.set_ylabel("phase")
    plt.plot(np.angle(csi))
    plt.ion()
    plt.pause(0.005)

def read_from_file(filename, filter_value=-1):
    file = open(filename, 'r')
    result = list()
    for line in file:
        temp = list()
        csi = line.strip().strip(';').split(';')
        for elem in csi:
                temp.append(complex(elem))

        if filter_value > 0:
            if np.mean(np.abs(temp)) > filter_value:
                result.append(np.abs(temp))
        else:
            result.append(np.abs(temp))

    file.close()
    return np.array(result)



# fuzzed1 = "C:/Users/seppe/Desktop/openwifi-self-cap/openwifi_csi_files/fuzzed_0_-20_0_20.txt"
# fuzzed2 = "C:/Users/seppe/Desktop/openwifi-self-cap/openwifi_csi_files/fuzzed_0_7_1_-33.txt"
# unfuzzed = "C:/Users/seppe/Desktop/openwifi-self-cap/openwifi_csi_files/unfuzzed.txt"

# fuzzed1 = read_from_file(fuzzed1)
# fuzzed2 = read_from_file(fuzzed2)
# unfuzzed = read_from_file(unfuzzed)



# # plot(fuzzed1, title=" fuzzed")
# plot_single(fuzzed2[0][2:-2], title="fuzzed")
# plot_single(unfuzzed[0][2:-2], title="normal")
# plot_single(fuzzed2[0][2:-2]/unfuzzed[0][2:-2], title="- fuzzing pattern")
# plot_single(fuzzed2[7][2:-2]/(fuzzed2[0][2:-2]/unfuzzed[0][2:-2]), title="fuzzing undone")


# try:
#     input()
#     exit(0)
# except KeyboardInterrupt:
#     exit(0)