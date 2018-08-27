# -*- coding: utf-8 -*-
"""
 Exploratory Data Analysis of CITES wildlife data


"""

import pandas as pd
import seaborn as sb
import os 

#create object file path to specify where data is stored
file_path = "C:/Users/curti/Documents/GitHub/Misc_PythonProjects/Data/CITES_WLDLIFE_TRADE/"

#list all files in a directory and print out stored result of files
files = os.listdir(file_path)
print(files)

#use list comprehension to concatenate the file path where the data is stored
#and the name of the different files in the data directory; print to see
#result
files_list = [file_path + f for f in files]
print(files_list)

#use Pandas concat method along with generator expression
wildlife_df = pd.concat((pd.read_csv(f) for f in files_list))
type(wildlife_df)

#now that the data is read, take a look at it

wildlife_df.head()
wildlife_df.shape
wildlife_df.describe()

#print a list of the column headers
print(list(wildlife_df))


#create some basic visualizations;

#looking at number of imports by year
wildlife_df['Year'].value_counts().plot(kind = "bar")
#most records are from 2016

#look at number of imports by class using base plotting commands
wildlife_df['Class'].value_counts().plot(kind = "bar")
#most imports are reptiles; followed by corals, mammals and birds

#create Seaborn count plot, this is more like R's ggplot
sb.countplot(data=wildlife_df, y = "Class")

