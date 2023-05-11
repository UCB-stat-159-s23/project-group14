# Group 14 Final Project

## Analysis of the relationship between cigarette sales per capita and median income by States in the US

Group 14: Zilin Zhang, Jiangyue Chen, Daniel Jang, Isabel Adelhardt

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-s23/project-group14.git/HEAD?labpath=main.ipynb)

## Project Overview

This project is to calculate and analyze the relationship between cigeratte sales per capita and median income in 51 different states in the United States from 2013 to 2019. In order to come out with a conclusion, we analyze and present the changing trend of cigeratte sales per capita and median income in 51 states from 2013 to 2019. Afterwards, we calculate the regression between two dataset and figure out the relationship between these two variables. 

## Data Source

Our team retrieves the tobacco sales data from [US Chronic Disease Indicators](https://chronicdata.cdc.gov/Chronic-Disease-Indicators/U-S-Chronic-Disease-Indicators-Tobacco/rrbt-bhen), and the median income data from [US Census Bureau](https://www2.census.gov/programs-surveys/cps/tables/time-series/historical-income-households/h08.xls). We then converted the data into cvs files using online file type converter, and put them into the folder `data/`.

## Project Website

Link to our Jupyter Book: https://ucb-stat-159-s23.github.io/project-group14

## Repository structure

`data/:`contains two raw data files and one processed data file

`output/:`contains the generated plots for EDA

`figures/:`contains png versions for html graphs generated in MapPlot.ipynb for displaying purposes

`project_tools/:`contains `tests/` and `dataformat.py` which are necessary files to build up our work in the analysis notebooks

`main.ipynb:` Main Notebook for our project, contains data analysis and interpretation

`sales-of-cigarette-each-state.ipynb:` contains data processing, plotting, and analyzing of the changing trend of cigarette sales in 51 different states from 2013 to 2019

`MapPlot.ipynb:` contains data processing, plotting (choropleth map plots), and analyzing of both average sales and median income in 51 different states from 2013 to 2019 (2015 omitted)

`LinearRegression.ipynb:` contains data processing, prediction, plotting, and analyzing the relationship between tobacco sales and average median income in specific states from 2013 to 2019 through linear regression

## Package Structure

The `project_tools` package is for reading in the tobacco sales data that was downloaded from the U.S. Chronic Disease Indicators as a data table. It then cleans the data table, so only relevant columns and rows are included. The package also reads in the average median income data that we downloaded from the U.S. Bureau of the Census, Current Population Survey, Annual Social, and Economic Supplements. We then clean the datatable, so we have only the necessary columns and add in the corresponding state's abbreviation. 

## Testing

The  `test_dataformat.py` tests our functions `dataformat.py` by making sure that the data that it returns is the correct dimensions.

## License

Our project employs the BSD 3-Clause License.



