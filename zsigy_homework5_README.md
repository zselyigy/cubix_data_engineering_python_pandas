# Homework 5 - Week 5
Created by István Gy. Zsély, version 0.1

# Project overview
This code was created during my participation in the [CUBIX Data Engineering course](https://courses.cubixedu.com/kepzes/data-engineer-23q4).

The aim is to demonstrate the knowledge about filtering / translating tasks using the Pandas library on multiple files and plotting pivot tables.

The following tasks are performed by the program, denoted in comments in the source code:

1. Use your “Read_parameters.ipynb” external program to read the parameter tables from “Parameters_Homework5.xlsx” (-> paramlist).

2. As the “Size” data in the 1st parameter table can be numeric and text values mixed, convert “Size” column to STRING data type (otherwise only the texts will be matched, e.g. “XL”).

3. The input folder pathsof the input files are in the 1stparameter table, loop through the rows of this table to do the following subtasks on each input file(put commentsin the program for each subtasks to explain them to the user):

    a. Filter the parameter dataframes to input file (paramlist -> paramlist_filt).

    b. Read the input file from its input folder path.
    
    c. Use the “Clean_order_data.ipynb” external program to clean it.

    d. Filter it on only the rows with the Sizes and Countries specified for the input file.
    
    e. Look upthe related Class Names of the class id’s (“H”, “M”, “L”), into a separate “Class Name” column.
    
    f. Remove “Class” column, as we only need “Class ID” column instead.
    
    g. Translate the column headers based on the lastparameter table with dictionary.
    
    h. The output folder should be a “2011” / “2012” / “2013” / “2014” subfolder inside the “Output” folder (based on input file’s name), the program should create these folders (if they do not exist).
    
    i. Use your “Export_to_csv.ipynb” external program to export the cleaned, filtered, translated dataframe to the output folder, the output file’s name should be the same as the input file, but with a “_cleaned_filtered_translated.csv” ending.

4. Read the “Orders_2011_cleaned_filtered_translated.csv” into a dataframea.Create a Pivot Tableon it, Rows: “Size”, Columns: “Class Name”, Values: “Revenue”, and write it out in cell outputb.Create a Stacked column (vertical bar) Charton the Pivot table, and write it out.

5. Create minimum three Markdowncells which give explanations about the goals of the program’s sections

6. At the end, write out the runtime, and a beep sound and a final printed message should notify the user.