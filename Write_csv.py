# export the dataframe to a csv file
# typically, we do not want to put the index numbers in the output file
df.to_csv(basepath + '\\' + outputfolder + '\\' + outputfile,
          index = False, sep = ';', encoding = 'utf-8')

# print(df)

print('Data cleaning done!')
