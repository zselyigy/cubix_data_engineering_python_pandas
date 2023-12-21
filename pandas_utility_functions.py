# function for the calculation of runtime in a string with a specific format
def calc_runtime(start, end):
    hour, remainder = divmod(end - start, 3600)
    minute, second = divmod(remainder, 60)
    return 'Runtime {:0>2}:{:0>2}:{:05.2f}'.format(int(hour), int(minute), second)


# function for the reading of the parameter file
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
    print('Paramlist file (' + paramfile + ') read.')
    return paramlist


# task 3 Create a “Clean_order_data.ipynb” external program, from only the data cleaning part of the Homework2 program (creating dimension tables is not needed now).
def clean_order_data(df):
    # import the pandas data analysis library
    import pandas as pd

    # remove the extra leading and tailing spacec from column 'Class'
    df['Class'] = df['Class'].str.strip(' ')

    # covert the type of column 'OrderDate" to DATETIME
    df['OrderDate'] = pd.to_datetime(df['OrderDate'], dayfirst = False)

    # conversion of the data of column 'LineTotal' to float
    # replace the comma decimal separator to dot
    df['LineTotal'] = df['LineTotal'].str.replace(',', '.')
    df['LineTotal'] = df['LineTotal'].astype(dtype = 'float64', errors = 'ignore')

    # separate the Size from the product name
    df[['Product_name', 'Size']] = df['ProductName'].str.split(', ', expand = True)
    # we do not need the original, uncleaned ProductName column
    df = df.drop(['ProductName'], axis = 1)
    # replace the 'Black', 'Red' and 'Blue' "sizes" with '-'
    pattern = r'\b(?:Black|Red|Blue)\b'
    df['Size'] = df['Size'].str.replace(pattern, '-', regex = True)
    # same with list:
    # colorlist = ['Black', 'Blue', 'Red']
    # df['Size'] = df['Size'].replace(colorlist, '-')
    # sort the df dataframe by “OrderDate” and “Country”
    df = df.sort_values(by = ['OrderDate', 'Country'])
    # reset the index
    df = df.reset_index(drop = True)

    # message to the user
    print('Dataframe cleaned.')

    return df


# task 2 Use your “Read_csv.ipynb” external program to read all input files.
def read_csv(basepath, inputfolder, inputfile):
    import pandas as pd

    # import the csv file to a dataframe
    df = pd.read_csv(basepath + '\\' + inputfolder + '\\' + inputfile, sep = ';', encoding = 'utf-8')

    return df


# task 9 Use your “Export_to_csv.ipynb” external program to export the cleaned, filtered dataframe to the output folder (“Output”).
def export_to_csv(basepath, outputfolder, outputfile, df):
    import os

    # create the output folder
    try:
        os.mkdir(basepath + '\\' + outputfolder)
    except:
        pass

    # export the dataframe
    df.to_csv(basepath + '\\' + outputfolder + '\\' + outputfile,
              index = False, sep = ';', encoding = 'utf-8')
    
    # message to the user
    print('csv file (' + outputfile + ') exported.')
