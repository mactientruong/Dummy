#!/usr/bin/python3
# -*- coding: utf-8 -*-
#File Name: text_file_process.py

#===================================== Revision history ================================
#=======================================================================================
#
#   UPDATE HISTORY     DATE        AUTHOR          MODIFIED POINT
#       Creation    2019.05.15  Mac Tien Truong     Create new

#This module is used to define the functions relate to text file process.
import os
import xlrd

#======================= Write the data into the text file =============================
#=======================================================================================
def writetextfile(textfilename, writemode, writedata):
    "This sub-function is used to write the data in the text file"

    #Procedure to write the data into the text file
    ojbtextfile = open(textfilename, writemode)
    ojbtextfile.write(writedata)
    ojbtextfile.close()

    return()

#======================== Read the data from the text file =============================
#=======================================================================================
def readtextfile(textfilename):
    "This file is used to read data from text file"

    #Procedure to read a text file
    if (os.path.exists(textfilename)):
        objtextfile = open(textfilename)
        receiveddata = objtextfile.read()
        objtextfile.close()

    return(receiveddata)

#======================== Get the data from the text file ==============================
#=======================================================================================
def getdatafromtextfile(textfilename, titlerownumber):
    "This function is used to get the data in the text file."

    #Define local variable(s) here
    data = ["None"]
    titlerownumbers = titlerownumber
    
    #procedure to get the data
    if (os.path.exists(textfilename)):
        objtextfile = open(textfilename)
        receiveddata = objtextfile.readlines()
        objtextfile.close()
        
        #Extract data from text file
        for each_data in range(len(receiveddata)):
            data.append(receiveddata[each_data].split(";")[-1])

        if(0 != len(data)):
            del data[0] #Remove the first element
        count = 0
        while (count < titlerownumbers):
            if (0 != len(data)):
                del data[0] #Remove the rows that are not related to expected data
            count = count + 1
    else:
        print("The file is not found")
    return (data)

#=============================== Delete the text file ==================================
#=======================================================================================
def deletetextfile(textfilename):
    "This function is used to delete the current text file"

    #Procedure to delete the current file, check if it is existed then delete else do nothing.
    if(os.path.exists(textfilename)):
        os.remove(textfilename)

    return()
