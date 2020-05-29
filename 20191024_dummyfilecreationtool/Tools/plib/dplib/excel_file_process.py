#!/usr/bin/python3
# -*- coding: utf-8 -*-
#File Name: excel_file_process.py

#===================================== Revision history ================================
#=======================================================================================
#
#   UPDATE HISTORY     DATE        AUTHOR          MODIFIED POINT
#       Creation    2019.05.15  Mac Tien Truong     Create new
#       Update      2019.07.16  Mac Tien Truong     Replaced access data via index of sheet by name of sheet.

#This module is use to define the functions relate to excel file process.
import os
import xlrd

#============================= Get the data from the excel files =======================
#=======================================================================================
def getdatafromexcelfiles (excel_file_name, sheet_name, col_name, row_title):
    "This function is used to get the data from the excel file"

    #Define the local variable(s) here
    l_excel_file_name = excel_file_name
    l_sheet_name = sheet_name
    l_col_name = col_name
    l_row_titles = row_title
    l_received_data = ["NULL"]
    l_column_index = 0

    #Procedure to get the data
    #Check the excel file that is either existed or not
    if(os.path.exists(l_excel_file_name)):
        #Open the excel file, choose the sheet
        l_obj_excel = xlrd.open_workbook(l_excel_file_name)
        l_obj_sheet = l_obj_excel.sheet_by_name(l_sheet_name)

        #Get number of colomn and row
        l_col_number = l_obj_sheet.ncols
        l_row_number = l_obj_sheet.nrows

        #Get all data of current sheet
        l_excel_data = [[l_obj_sheet.cell_value(l_rows, l_cols) for l_cols in \
                         range(l_obj_sheet.ncols)] for l_rows in range(l_obj_sheet.nrows)]

        #Find the column that we would like to get the data
        l_index = 0
        while (l_index < l_col_number):
            if (l_col_name == l_obj_sheet.cell_value(l_row_titles, l_index)):
                l_column_index = l_index
                break
            else:
                l_index = l_index + 1

        #Check the column
        if(l_index == l_col_number):
            print ("Could not find the column name: ", l_col_name)
        else:
            #Remove the N/A symbol and the corresponding column name
            l_count_element = 0
            for l_row_index in range(l_obj_sheet.nrows):
                if((l_obj_sheet.cell_value(l_row_index, l_column_index) != "N/A") and \
                   (l_obj_sheet.cell_value(l_row_index, l_column_index) != l_col_name)):
                    l_received_data.append(l_obj_sheet.cell_value(l_row_index, l_column_index))
                    l_count_element = l_count_element + 1

            if(l_count_element > 0 ):
                del l_received_data[0]   #Remove the NULL element
    else:
        print("Could not find out the file name: ", l_excel_file_name)
      
    return (l_received_data)

#================================== Convert the data ===================================
#=======================================================================================
def convertdata(array_data, symbol_plit, ending_symbol):
    "This function is used to convert the data"

    #Define the local variable(s) here
    l_array_data = array_data
    l_symbol_plit = symbol_plit
    l_ending_symbol = ending_symbol

    #Procedure to convert the data here
    for l_each_data in range(len(l_array_data)):
        if(l_ending_symbol == l_array_data[l_each_data].split(l_symbol_plit)[-1]):
            l_temp = l_array_data[l_each_data].split(l_symbol_plit)
            l_temp1 = l_ending_symbol + l_temp[0]
            del l_temp[len(l_temp)-1]
            for i in range(len(l_temp)):
                l_temp1 = l_temp1 + "_" + l_temp[i]

            l_array_data[l_each_data] = l_temp1

    return (l_array_data)
