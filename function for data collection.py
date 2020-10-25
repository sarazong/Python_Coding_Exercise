#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 06:27:25 2020

@author: sarazzzz
"""

def collect_data(pdf, start_county, end_county):
    """Read in a PDF file containning covid daily count data in a table. 
    Create hierarchical indices to aggregate covid counts for each county by race and by ethnicity separately.
    Return two excel files for race and ethnicity data.
    
    Args:
        pdf: name of pdf file downloaded from state public health department.
        start_county: beginning name of the county in which data is of interest.
        end_county: end name of the county in which data is of interst.
        
    Returns: 
        Two excel files.
    """
    
    import tabula 
    import pandas as pd

    path = "/Users/sarazzzz/Desktop/"
    daily_data = tabula.read_pdf(path + pdf)

    # the second row of the dataframe contains column names, make the row column indices
    col_name = daily_data.iloc[1]
    daily_data.columns = col_name

    # remove the first row in the dataframe since it's not properly imported from the PDF
    # remove the second row since they are column names now
    daily_data = daily_data.iloc[2:]

    # set the first two columns in the dataframe as row indices
    daily_data = daily_data.set_index(["County", "Total Cases"])
    

    # create MultiIndex for columns
    ethnicity = ["Not Hispanic", "Not Hispanic", "Not Hispanic", "Not Hispanic", "Not Hispanic", "Not Hispanic",
              "Hispanic", "Hispanic", "Hispanic", "Hispanic", "Hispanic", "Hispanic",
              "Unknown Ethnicity", "Unknown Ethnicity", "Unknown Ethnicity", "Unknown Ethnicity", "Unknown Ethnicity", "Unknown Ethnicity"]
    race = list(daily_data.columns)
    daily_data.columns = pd.MultiIndex.from_arrays([ethnicity, race], names = ["ethnicity", "race"]) 

    # convert all the columns to numeric       
    daily_data = daily_data.apply(pd.to_numeric)

    # create the desired subset of data
    subset = daily_data.loc[start_county : end_county]

    race_sum = subset.sum(level = "race", axis = 1)

    ethnicity_sum = subset.sum(level = "ethnicity", axis = 1)

    # save final dataframes into excel files
    writer = pd.ExcelWriter(path + "Mississipi_covid_case_" + pdf.split(sep = ".")[0] + ".xlsx", engine = "xlsxwriter")
    race_sum.to_excel(writer, sheet_name = "race_sum")
    ethnicity_sum.to_excel(writer, sheet_name = "ethnicity_sum")
    
    return writer.save()
