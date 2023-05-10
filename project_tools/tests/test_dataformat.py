import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import warnings
import pandas as pd
import numpy as np
from IPython.display import HTML
from project_tools import dataformat
warnings.filterwarnings('ignore')

def test_tobacco_data_import():
    data = dataformat.tobacco_data_import()
    assert data.shape == (306, 6)


def test_income_data_import():
    data = dataformat.income_data_import()
    assert data.shape == (51, 10)