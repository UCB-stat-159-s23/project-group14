import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import warnings
import pandas as pd
import numpy as np
warnings.filterwarnings('ignore')

def tobacco_data_import():
    '''
    This function process the tobacco data that we downloaded from U.S.
    Chronic Disease Indicators (CDI).
    It reads the U.S._Chronic file _Disease_Indicators__Tobacco.csv file
    and returns a preferrable data frame that we will use to plot graphs
    and to analyze.
    '''
    data = pd.read_csv('data/U.S._Chronic_Disease_Indicators__Tobacco.csv', low_memory=False)

    # filter question
    data = data[data["Question"] == "Sale of cigarette packs"]

    # filter columns
    data = data[['YearStart', 'LocationAbbr', 'LocationDesc', 'Question', 'DataValueUnit', 'DataValue']]
    data = data.groupby(['YearStart', 'LocationDesc']).sum().reset_index()

    # remove states GU, PR, US, VI since they are not actual states.
    data = data.loc[data['DataValue'] != 0.0]
    data.to_csv("data/states_sales.csv")

    return data


def income_data_import():
    '''
    This function process the median income data that we downloaded from U.S.
    Bureau of the Census, Current Population Survey, Annual Social and
    Economic Supplements.
    It reads in the median_income.csv file and returns a preferrable data frame
    that we will use to plot graphs and to analyze.
    '''
    median_DATA = pd.read_csv('data/median_income.csv')
    cols_drop = median_DATA.columns[median_DATA.columns.str.contains("Standard")]
    median_income = median_DATA.drop(columns=cols_drop).set_index("Location")
    # drop 2017(40) and 2013(39)
    median_income = median_income.drop(median_income.columns[[0, 1, 4, 9]], axis = 1)
    us_state_to_abbrev = {
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "District of Columbia": "DC",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "Washington": "WA",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY"
    }

    median_income = median_income.reset_index().copy()

    median_income.iloc[:, 1:len(median_income)] = median_income.iloc[:, 1:len(median_income)].replace(',','', regex=True).astype(float)
    median_income["avg_med_income"] = median_income.iloc[:, 1:len(median_income)].mean(axis = 1)

    # Abbreviate the States for plotly geographical mapping
    median_income["state"] =  median_income["Location"]
    median_income = median_income.replace({"state": us_state_to_abbrev}).drop(0)

    # median_income.columns.values[7] = '2013 Median income'
    median_income = median_income.rename(columns={median_income.columns.tolist()[7]:'2013 Median income'})

    return median_income
