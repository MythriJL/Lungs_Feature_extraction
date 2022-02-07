import matplotlib.pyplot as plt
import pydicom
import pydicom.data

def read(base, pass_dicom):
    filename = pydicom.data.data_manager.get_files(base, pass_dicom)[0]
    ds = pydicom.dcmread(filename)
    return ds
