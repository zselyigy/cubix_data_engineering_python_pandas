# import the pandas data analysis library
import pandas as pd

# base path related variables
basepath = r'.\Python_DA'
inputfolder = 'Input'
inputfile = 'Source1.csv'
outputfolder = 'Output'
outputfile = 'Revenues.csv'

# read data from a csv file into a dataframe
df = pd.read_csv(basepath + '\\' + inputfolder + '\\' + inputfile, sep = ';', encoding = 'utf-8')
# print the number of rows and columns, the total number of cells and the column titles of the dataframe
print(df.shape, df.size, df.columns)