# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 16:17:43 2019

@author: curti
"""

#bring in required modules
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import datetime import datetime

#set some important directory locations as variables

#overall project directory
proj_dir = "C:/Practice_projects/WWII_bombing_ops"

#data directory
data_dir = "/Data"

#script directory
scripts_dir = "/Scripts"

#output file directory; for things like flat file outputs
out_files_dir = "/Outputs/Files"

#output figure directory
out_fig_dir = "/Outputs/Plots"

#read in raw data file
raw = pd.read_csv(proj_dir + data_dir + "/operations.csv", sep = ",", header = [0], encoding = 'latin-1')

#change the column headers to all lowercase
raw.columns = raw.columns.str.lower()

#replace all blank spaces in the column names with underscores
raw.columns = raw.columns.str.replace(" ", "_")

#get list of column names
col_names = list(raw.columns)

#use for loop to loop through the columns in dataframe raw and if the column
#is missing more than 55% of it's data then drop it from the dataframe 'raw
for col in col_names:
    if ((raw[col].isna().sum()/raw.shape[0])*100) > 55.0:
        raw.drop(columns = col, inplace = True)
    else:
        raw[col]

#modify plotting parameters for pyplot figures
plt.rcParams["figure.figsize"] = [16,9]
        
#look at histograms of the remaining numeric variables
raw.hist()

#create a new column month from the dates in 'mission_date' column and then covert to text 
raw['mission_date'] = pd.to_datetime(raw['mission_date'])
raw['month'] = raw['mission_date'].apply(lambda x: datetime.strftime(x, '%B'))
raw['year'] = raw['mission_date'].dt.year


#look at number of unique entries for each of the categorical variables
raw.select_dtypes(include = ['object']).apply(lambda x: x.nunique())

#create a list of the column names in raw where the column type is a string
raw_cats = list(raw.select_dtypes(include = ['object']).columns)

#create a list of the column names in raw where the column type is numeric
raw_nums = list(raw.select_dtypes(include = ['number']).columns)

#create a correlation matrix for the numeric variables       
corr_mat = raw[raw_nums].corr()  

#create a heatmap of the correlation matrix 'corr_mat'
sns.heatmap(corr_mat, annot = True, fmt = '.1g')

#define a function that will create a count plot for each of the categorical
#variables in dataframe 'raw'; limit to top 15 categories because some categorical
#variables have tons of categories
def cplt_func(x):
    f, ax = plt.subplots()
    f = sns.countplot(y = x, data = raw[raw_cats], color = 'c', order = x.value_counts(ascending = False).iloc[:15].index)
    return f

#apply the 'cplt_func' to raw
raw[raw_cats].apply(lambda x: cplt_func(x))
