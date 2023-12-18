# Homework 4 - Week 4
Created by István Gy. Zsély, version 0.1

# Project overview
This code was created during my participation in the [CUBIX Data Engineering course](https://courses.cubixedu.com/kepzes/data-engineer-23q4).

The aim is to demonstrate the knowledge about transformation / cleaning tasks using the Pandas library on multiple files.

The following tasks are performed by the program, denoted in comments in the source code:

1. Use your “Read_parameters.ipynb” external program to read the parameter tables from “Parameters_Homework4.xlsx”.

2. Loop through the input files of the input folder, use your “Read_csv.ipynb” external program to read all of them, and append them into 1 dataframe.

3. Create a “Clean_order_data.ipynb” external program, from only the data cleaning part of the Homework2 program (creating dimension tables is not needed now).

4. Run this “Clean_order_data.ipynb” external program to clean the dataframe.

5. As the “Size” data in the 1st parameter table can be numeric and text values mixed, convert “Size” column to STRING data type (otherwise only the texts will be matched, e.g. “XL”).

6. Filter the dataframe on only the rows with the Sizes and Countriesin the parameter file.

7. Look up the related Class Names of the class id’s (“H”, “M”, “L”) from the parameter file, into a separate “Class Name” column in the dataframe.

8. Remove “Class” column, as we only need “Class ID” column instead (to make it easy to distinguish it from Class Name).

9. Use your “Export_to_csv.ipynb” external program to export the cleaned, filtered dataframe to the output folder (“Output”), the output file’s name should be: “Orders_all_periods_cleaned_filtered.csv”.

10. Create minimum three Markdowncells which give explanations about the goals of the program’s sections.

11. At the end, write out the runtime, and a beep sound and a final printed message should notify the user.