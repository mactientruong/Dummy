#!/usr/bin/python3
# -*- coding: utf-8 -*-
#File Name: text_file_process.py

#===================================== Revision history ================================
#=======================================================================================
#
#   UPDATE HISTORY     DATE        AUTHOR          MODIFIED POINT
#       Creation    2019.05.17  Mac Tien Truong     Create new

#This module is use to define the functions relate to text file process.
import os
import xlrd
#=============================== Delete the text file ==================================
#=======================================================================================
def deletetextfile(text_file_name):
    "This function is used to delete the current text file"

    #Define local variable(s) here
    l_text_file_name = text_file_name

    #Procedure to delete the current text file
    #Check if it is existed then delete else do nothing
    if(os.path.exists(l_text_file_name)):
        os.remove(l_text_file_name)

    return()


#========================== Write data into the text file ==============================
#=======================================================================================
def writetextfile(text_file_name, mode_write, data_write):
    "This function is used to write the data in the text file"

    #Define the local variable(s) here
    l_text_file_name = text_file_name
    l_mode_write = mode_write
    l_data_write = data_write

    #Procedure to write the data into the text file
    l_ojb_text_file = open(l_text_file_name, l_mode_write)
    l_ojb_text_file.write(l_data_write)
    l_ojb_text_file.close()

    return()

#========================== Read data from the text file ===============================
#=======================================================================================
def readtextfile(text_file_name):
    "This file is used to read data from text file"

    #Define the local variable(s) here
    l_text_file_name = text_file_name
    l_received_data = ["NULL"]

    #Procedure to read a text file
    if (os.path.exists(l_text_file_name)):
        l_obj_text_file = open(l_text_file_name)
        l_data_temp = l_obj_text_file.readlines()
        l_obj_text_file.close()
        for each_data in l_data_temp:
            temp = each_data.split("\n")[0]
            l_received_data.append(temp)
        del l_received_data[0]
    else:
        print("Could not find out the file name:", text_file_name)

    return(l_received_data)

#============================== Remove the duplicated data =============================
#=======================================================================================
def removeduplicate(data_list):
    "This function is used to remove the duplicated data"

    l_data_list = data_list
    l_count1 = 0
    while (l_count1 < len(l_data_list) - 1):
        l_temp = l_data_list[l_count1]
        l_count2 = l_count1 + 1
        while (l_count2 < len(l_data_list)):
            if(l_temp == l_data_list[l_count2]):
               del l_data_list[l_count2]
            l_count2 = l_count2 + 1
        l_count1 = l_count1 + 1

    return(l_data_list)
