#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 06:27:25 2020

@author: sarazzzz
"""
import tabula
import pandas as pd

def collect_data(pdf, start_county, end_county):
    """Reads in table from a PDF file, and converts data to excel files.
    
    Args:
        pdf: name of pdf file as a string.
        start_county: name of the county at the beginning as a string.
        end_county: name of the county at the end as a string.
        
    Returns: 
        Two excel files.
    """

    path = "/Users/sarazzzz/Desktop/"
    daily_data = tabula.read_pdf(path + pdf)

    #convert the second row of the dataframe into column names
    col_name = daily_data.iloc[1]
    daily_data.columns = col_name
    daily_data = daily_data.iloc[2:]

    #set the first two columns in the dataframe as row indices
    daily_data = daily_data.set_index(["County", "Total Cases"])
    
    #create MultiIndex for columns
    cat_1 = ["Not Hispanic"]
    cat_2 = ["Hispanic"]
    cat_3 = ["Unknown Ethnicity"]
    ethnicity = cat_1 * 6 + cat_2 * 6 + cat_3 * 6
    race = list(daily_data.columns)
    daily_data.columns = pd.MultiIndex.from_arrays([ethnicity, race], names = ["ethnicity", "race"]) 

    #sum data by race or ethnicity
    daily_data = daily_data.apply(pd.to_numeric)
    subset = daily_data.loc[start_county : end_county]

    race_sum = subset.sum(level = "race", axis = 1)
    ethnicity_sum = subset.sum(level = "ethnicity", axis = 1)

    #save final dataframes into excel files
    writer = pd.ExcelWriter(path + "Mississipi_covid_case_" + pdf.split(sep = ".")[0] + ".xlsx",
                            engine = "xlsxwriter")
    race_sum.to_excel(writer, sheet_name = "race_sum")
    ethnicity_sum.to_excel(writer, sheet_name = "ethnicity_sum")
    
    return writer.save()
