# Homework 2 - Week 2
Created by István Gy. Zsély, version 0.2

# CHANGE LOG
- The uncleaned ProductName column removed.
- The unecessary spaced from the Sie column removed.

# Project overview
This code was created during my participation in the [CUBIX Data Engineering course](https://courses.cubixedu.com/kepzes/data-engineer-23q4).

The aim is to demonstrate the knowledge about the basic features of the [Python pandas library](https://pandas.pydata.org/).

The following tasks are performed by the program, denoted in comments in the source code:

1. The input folder: “Input”, the input file: “Orders_2011.csv” inside it.
2. The output folder should be the “Output” folder.
3. Use your “Read_csv.ipynb” external program to read theinput file into a dataframe (“df”).
4. Remove the extra trailing & leading spaces from the values of “Class” column (because there can be extra spaces, e,g: “H “, “M “, “L “).
5. Convert the “OrderDate” column (which is of string data type) to DATETIME type.
6. Convert the “LineTotal” column to FLOAT data type (beware of that the values should have a decimal POINT instead of a decimal COMMA).
7. Put the size of the products (which is in the end of product name, separated by a comma) into a separate “Size” column (ifthe “Size” column shows “Black”, “Red” or “Blue”, those should be replaced to “-“).
8. Create a dimension table (“df_sizes”) of the values of the “Size” column, sorted in ascending order, with an ID index column, and write it out in a cell’s output.
9. Sort the “df” dataframe by “OrderDate” and “Country”, and reset the index.
10. Use your “Export_to_csv.ipynb” external program to export the final “df” dataframe to the output folder, the output file’s name should be the same as the input file, but with a “_cleaned.csv” ending.
11. Create minimum one Markdowncell which gives explanations about the program’s goal.
12. At the end, a final printed message should notify the user.