import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np


def import_data(df):
    """
    
    Input: Stored path variable
    
    Return: Dataframe
    
    """
    
    print("Generating dataframe")
    return pd.read_csv('data/states_sales.csv')



def save_data(df):
    """
    
    Save the data
    
    """
    print("Saving data")
    return data.to_csv(df index=True)



def df_len(df):
    """
    
    Input: Dataframe
    
    Return: Size (row and column) of the dataframe
    
    
    """
    print("Printing its size")
    print("Row(s): ", df.shape[0], "Column(s): ", df.shape[0])
