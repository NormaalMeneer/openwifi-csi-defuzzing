from math import inf
import numpy as np
from CSIKit.reader import ATHBeamformReader
from CSIKit.tools.get_info import display_info
from CSIKit.util import csitools

def read_csi_file(file):
    my_reader = ATHBeamformReader()
    csi_data = my_reader.read_file(file)
    csi_matrix, no_frames, no_subcarriers = csitools.get_CSI(csi_data, extract_as_dBm=False)
    cleaned_csi_matrix = clean_csi_matrix(csi_matrix)
    return cleaned_csi_matrix

def print_file_info(file):
    display_info(file)

def clean_csi_matrix(matrix):
    make_complex = lambda sub_list : np.complex(sub_list[0][0],sub_list[0][1])
    result = list()
    for i,item in enumerate(matrix):
        # niet meer flippen!!!
        result.append(np.abs(list(map(make_complex,item))))
    return result
