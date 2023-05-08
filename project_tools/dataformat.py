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
warnings.filterwarnings('ignore')


def tobacco_data_import(data):
    data = pd.read_csv('data/U.S._Chronic_Disease_Indicators__Tobacco.csv', dtype='object')
    return data


def income_data_import(data):
    data = pd.read_csv('data/median_income.csv')
    return data