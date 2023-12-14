import pandas as pd

paramfolderpath = r'.\Python_DA'
paramfile = 'Parameters.xlsx'
paramfile_sheet = 'Parameter tables'

df_param = pd.read_excel(paramfolderpath + '\\' + paramfile, sheet_name = paramfile_sheet, usecols = 'A:B')
print(df_param)
