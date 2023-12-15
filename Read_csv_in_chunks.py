import pandas as pd

# base path related variables
basepath = r'.\Python_DA'
inputfolder = 'Output\\All periods'
inputfile = 'Revenues_all_periods.csv'
newinputfile = 'Revenues_all_periods_by_chunks.csv'

columnlist = ['Product', 'Customer', 'Date', 'Revenue']
customerlist = [' ABC Travel ', ' Artec']

# read csv in chunks
chunkrows = 20
chunks = pd.read_csv(basepath + '\\' + inputfolder + '\\' + inputfile, sep = ';', encoding = 'utf-8',
                 usecols= columnlist, chunksize= chunkrows, iterator= True)

firstchunk = True
for df in chunks:
    # filter column to values which are in the list
    df = df[df['Customer'].isin(customerlist)]
    df['Customer'] = df['Customer'].str.strip(' ')
    print(df)
    # export data in csv file
    if firstchunk:  # a new file if this is the first chunk
        df.to_csv(basepath + '\\' + inputfolder + '\\' + newinputfile, index = False, sep = ';', encoding = 'utf-8')
        firstchunk = False
    else:           # append if this is not the first chunk
        df.to_csv(basepath + '\\' + inputfolder + '\\' + newinputfile, mode= 'a', header= False, index = False, sep = ';', encoding = 'utf-8')
    
