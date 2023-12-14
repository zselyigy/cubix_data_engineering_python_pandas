# import the pandas data analysis library
import pandas as pd
import export_to_excel as ee

# create a list of all columns we go through
columnlist = ['Product', 'Customer', 'Salesperson']

for mycolumn in columnlist:
    # reduce the dataframe to a specific column
    df_export = df[[mycolumn]]
    # sort the content in alphabetical order
    df_export = df_export.sort_values(by = [mycolumn])
    # remove the duplicated
    df_export = df_export.drop_duplicates()

   # drop the old indexes, but introduce new ones
    df_export = df_export.reset_index(drop = True)

    # insert an ID column
    df_export.insert(0, mycolumn + 'ID', df_export.index + 1)

    # export the dataframe to a csv file
    # typically, we do not want to put the index numbers in the output file
    df_export.to_csv(basepath + '\\' + outputfolder + '\\' + mycolumn + 's.csv',
            index = False, sep = ';', encoding = 'utf-8')
    # export the dataframe to an excel file
    outputsheet = mycolumn + 's'
    ee.dataframe_export_to_new_excel(df_export, basepath, outputfolder, mycolumn + 's.xlsx', outputsheet)
    
    # export the dataframe to a multipleexcel file
    # export first to a new excel and add the sheets one by one later
    if mycolumn == columnlist[0]:
        ee.dataframe_export_to_new_excel(df_export, basepath, outputfolder, 'Dimension_tables.xlsx', outputsheet)
    else:
        ee.dataframe_export_to_existing_excel(df_export, basepath, outputfolder, 'Dimension_tables.xlsx', outputsheet)
