import pandas as pd

paramfolderpath = r'.\Python_DA'
paramfile = 'Parameters.xlsx'
paramfile_sheet = 'Parameter tables'

df_param = pd.read_excel(paramfolderpath + '\\' + paramfile, sheet_name = paramfile_sheet, usecols = 'A:B')
print(df_param) # all rows are read, but most of them do not contain information

# drop the rows where there is no value in column 'Input file'
df_param = df_param.dropna(subset= ['Input file'])
print(df_param)
