# import the pandas data analysis library
import pandas as pd
import os

# base path related variables
basepath = r'.\Python_DA'
inputfolder = 'Input'
inputfile = 'Source1.csv'
outputfolder = 'Output'
outputfile = 'Revenues.csv'

#exec(compile(source=open('Read_csv.py').read(), filename='Read_csv.py', mode='exec'))
# read data from a csv file into a dataframe
df = pd.read_csv(basepath + '\\' + inputfolder + '\\' + inputfile, sep = ';', encoding = 'utf-8')

exec(compile(source=open('week2_Clean_data2.py').read(), filename='week2_Clean_data2.py', mode='exec'))
#exec(compile(source=open('Write_csv.py').read(), filename='Write_csv.py', mode='exec'))

# reduce the dataframe to a specific column
df_products = df[['Product']]
# sort the content in alphabetical order
df_products = df_products.sort_values(by = ['Product'])
# remove the duplicated
df_products = df_products.drop_duplicates()

# # another possibility
# # remove the fuplicated regarding a given column using the subset paramter
# df_products2 = df.drop_duplicates(subset= ['Product'])
# # reduce the dataframe to a specific column
# df_products2 = df_products2[['Product']]

# drop the old indexes, but introduce new ones
df_products = df_products.reset_index(drop = True)

# insert an ID column
df_products.insert(0, 'ProductID', df_products.index + 1)


# the same for the Customers and the Salesperson

# reduce the dataframe to a specific column
df_customers = df[['Customer']]
# sort the content in alphabetical order
df_customers = df_customers.sort_values(by = ['Customer'])
# remove the duplicated
df_customers = df_customers.drop_duplicates()

# # another possibility
# # remove the fuplicated regarding a given column using the subset paramter
# df_customers2 = df.drop_duplicates(subset= ['Customer'])
# # reduce the dataframe to a specific column
# df_customers2 = df_customers2[['Customer']]

# drop the old indexes, but introduce new ones
df_customers = df_customers.reset_index(drop = True)

# insert an ID column
df_customers.insert(0, 'CustomerID', df_customers.index + 1)

# reduce the dataframe to a specific column
df_salespersons = df[['Salesperson']]
# sort the content in alphabetical order
df_salespersons = df_salespersons.sort_values(by = ['Salesperson'])
# remove the duplicated
df_salespersons = df_salespersons.drop_duplicates()

# # another possibility
# # remove the fuplicated regarding a given column using the subset paramter
# df_salespersons2 = df.drop_duplicates(subset= ['Salesperson'])
# # reduce the dataframe to a specific column
# df_salespersons2 = df_salespersons2[['Salesperson']]

# drop the old indexes, but introduce new ones
df_salespersons = df_salespersons.reset_index(drop = True)

# insert an ID column
df_salespersons.insert(0, 'SalespersonID', df_salespersons.index + 1)

print(df_products)
print(df_customers)
print(df_salespersons)

# export the dataframe to a csv file
# typically, we do not want to put the index numbers in the output file
df_products.to_csv(basepath + '\\' + outputfolder + '\\' + 'Products.csv',
          index = False, sep = ';', encoding = 'utf-8')
df_customers.to_csv(basepath + '\\' + outputfolder + '\\' + 'Customers.csv',
          index = False, sep = ';', encoding = 'utf-8')
df_salespersons.to_csv(basepath + '\\' + outputfolder + '\\' + 'Salespersons.csv',
          index = False, sep = ';', encoding = 'utf-8')

# export the dataframe to an excel file
df_products.to_excel(basepath + '\\' + outputfolder + '\\' + 'Products.xlsx',
          index = False, sheet_name= 'Products')
df_customers.to_excel(basepath + '\\' + outputfolder + '\\' + 'Custormes.xlsx',
          index = False, sheet_name= 'Customers')
df_salespersons.to_excel(basepath + '\\' + outputfolder + '\\' + 'Salespersons.xlsx',
          index = False, sheet_name= 'Salespersons')

# export the dataframe to a multipleexcel file
with pd.ExcelWriter(basepath + '\\' + outputfolder + '\\' + 'Dimension_tables.xlsx') as writer:
    df_products.to_excel(writer, index = False, sheet_name= 'Products')
    df_customers.to_excel(writer, index = False, sheet_name= 'Customers')
    df_salespersons.to_excel(writer, index = False, sheet_name= 'Salespersons')
