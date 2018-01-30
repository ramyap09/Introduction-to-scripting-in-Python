This repository contains the assignments for the "Introduction to scripting in Python" specialization offered by Rice University at the Coursera platform. The specialization has 4 courses, and the assignements for each course are arranged in 4 respective folders here. The details of the assignments are given below.

1. #### /Python data analysis/week3_project_working_with_csvfiles.py 

This program contains a group of functions to read data from CSV (Comma Separated Value) files in the form of list of dictionaries and nested dictionary and to write data into CSV files.

2. #### /Python data analysis/week4_project_analyzing_baseball_data.py

This program analyzes the baseball data to calculate various batting statistics parameters for the players. There are 2 CSV files - one containing the player details and the second containing the batting details - as input to this program. Program is written in a way that any files can be input to it, but they should have columns specified as the Values in the baseballdatainfo dictionary given in the program.

3. #### /Python data representations/week4_project_diff_between_files.py

This program does the file comparison. If we input two text files to this program, it will give us the location of the first difference between the files, by doing a character by character comparison.

4. #### /Python data visualization/week2_project_basic_XYplots.py

If we input World bank GDP data in text format to this program, it will create some basic XY plots in SVG format depcting how GDP of specifed countries varies in the specified year range. The input file should have the World bank GDP data over several years, along the Country names and Country codes and make sure that the keys in the dictionary gdpinfo are updated according the input data file. 

5. #### /Python data visualization/week3_project_unify_data_and_maps_1.py

Once we input the World bank GDP data file, this program creates a world map plot of the GDP data for the given year and writes it to a file of SVG format. The Values in the dictionary named gdpinfo, specified in the program should match with the GDP data file name and it's various column names. Note that, here the country names in the plotting library (here, pygal) and in the World bank GDP data file are matched to fetch the GDP values of countries.

#### /Python data visualization/week4_project_unify_data_and_maps_2.py

Like week3_project_unify_data_and_maps_1.py this program also creates the world map plot of the GDP data for the specified year. Note that in the plot library and in the GDP datafile, the same country names might have been written in different forms/ways. This may lead to missing out certain countries' data in the process of fetching the data by matching the country names. So, along with the GDP data file, this program takes one more textfile as input which contains the country codes for the world countries in various formats including the plot library format and the GDP data file format. Thus using this country code file, instead of matching the country names, the country codes between plot library and GDP data file are matched to fetch the GDP data from the GDP file and tag it on the world map. The Values in the dictionary codefile specified in the program are updated based on the name and column names of the country code file.

#### Python programming essentials/week4_project_working_with_datetime.py

This program contains functions processing the dates to output the age in days, once we input the date of birth in the specified format.






