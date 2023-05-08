import numpy as np
from scipy.io import wavfile
from scipy import signal
from scipy.interpolate import interp1d
from scipy.signal import butter, filtfilt, iirdesign, zpk2tf, freqz
import h5py
import json
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import warnings
import pandas as pd
import numpy as np
from project_tools import dataformat
warnings.filterwarnings('ignore')


def test_tobacco_data_import():
    data = pd.read_csv('data/U.S._Chronic_Disease_Indicators__Tobacco.csv', dtype='object')
    data = dataformat.tobacco_data_import(data)
    assert data.shape == (59396, 33)

    
def test_income_data_import():
    data = pd.read_csv('data/median_income.csv')
    data = dataformat.income_data_import(data)
    assert data.shape == (52, 23)