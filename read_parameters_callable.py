def read_parameters(paramfolderpath, paramfile, paramfile_sheet, usedcolumnlist):
    import pandas as pd

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

    # print(paramlist)
    print('Paramlist file read.')
    return paramlist