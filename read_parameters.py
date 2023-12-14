import pandas as pd

paramfolderpath = r'.\Python_DA'
paramfile = 'Parameters.xlsx'
paramfile_sheet = 'Parameter tables'

# df_param = pd.read_excel(paramfolderpath + '\\' + paramfile, sheet_name = paramfile_sheet, usecols = 'A:B')
# print(df_param) # all rows are read, but most of them do not contain information

# # drop the rows where there is no value in column 'Input file'
# df_param = df_param.dropna(subset= ['Input file'])
# print(df_param)

# df_param = pd.read_excel(paramfolderpath + '\\' + paramfile, sheet_name = paramfile_sheet, usecols = 'D:E')
# print(df_param) # all rows are read, but most of them do not contain information

# # the 'Input file' column comes as 'Input file.1' as there are three columns with the same name, but this is the second one
# df_param.rename(columns= lambda x: x.split('.')[0], inplace= True)

# # drop the rows where there is no value in column 'Input file'
# df_param = df_param.dropna(subset= ['Input file'])
# print(df_param)

usedcolumnlist = ['A:B', 'D:E', 'G:H', 'J:L']
paramlist = []

for mycolumns in usedcolumnlist:
    # read the given columns from the excel file
    df_param = pd.read_excel(paramfolderpath + '\\' + paramfile, sheet_name = paramfile_sheet, usecols = mycolumns)
    # remove the . label from the multiple headers
    df_param.rename(columns= lambda x: x.split('.')[0], inplace= True)
    # drop the empty rows
    df_param = df_param.dropna(subset= [df_param.columns[0]])
    # add the dataframe to the list of paramters
    paramlist.append(df_param)

print(paramlist)