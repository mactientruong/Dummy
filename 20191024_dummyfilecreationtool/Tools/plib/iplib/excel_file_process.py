#!/usr/bin/python3
# -*- coding: utf-8 -*-
#File Name: excel_file_process.py

#===================================== Revision history ================================
#=======================================================================================
#
#   UPDATE HISTORY     DATE        AUTHOR          MODIFIED POINT
#       Creation    2019.05.15  Mac Tien Truong     Create new
#       Update      2019.07.16  Mac Tien Truong     Replaced access data via index of sheet by name of sheet.

#This module is use to define the function relate to excel file process.
import os
import xlrd

#============================== Get the data from the excel files ======================
#=======================================================================================
def getdatafromexcelfiles (excelfilename, sheetname, colname, rowtitle):
    "This function is used to get the data from the excel file"

    #Define the local variable(s) here
    receiveddata = ["NULL"]
    columnindex = 0
    rowtitles = rowtitle

    #Procedure to get the data
    #Check the excel file is existed or not
    if(os.path.exists(excelfilename)):
        #Open the excel file, chose the sheet
        objexcel = xlrd.open_workbook(excelfilename)
        objsheet = objexcel.sheet_by_name(sheetname)

        #Get number of colomn and row
        colnumber = objsheet.ncols
        rownumber = objsheet.nrows

        #Get all data of current sheet
        exceldata = [[objsheet.cell_value(rows, cols) for cols in range(objsheet.ncols)] \
                      for rows in range(objsheet.nrows)]

        #Find the column that we would like to get the data
        index = 0
        while (index < colnumber):
            if (colname == objsheet.cell_value(rowtitles, index)):
                columnindex = index
                break
            else:
                index = index + 1

        #Check the column
        if(index == colnumber):
            print ("The column is not found")
        else:
            countelement = 0
            for rowindex in range(objsheet.nrows):
                if((objsheet.cell_value(rowindex, columnindex) != "N/A") and \
                   (objsheet.cell_value(rowindex, columnindex) != colname)):
                    receiveddata.append(objsheet.cell_value(rowindex, columnindex))
                    countelement = countelement + 1

            if(countelement > 0 ):
                del receiveddata[0]   #Remove the NULL element
    else:
        print("The current file is not existed")
      
    return (receiveddata)

#================================== Convert the data ===================================
#=======================================================================================
def convertdata(arraydata, symbolplit, endingsymbol):
    "This function is used to convert the label that has f or mf in the end of its name"

    data = arraydata
    endsymbol = endingsymbol
    for each_data in range(len(data)):
        if(endsymbol == data[each_data].split(symbolplit)[-1]):
            temp = data[each_data].split(symbolplit)
            temp1 = endsymbol + temp[0]
            del temp[len(temp)-1]
            for i in range(len(temp)-1):
                temp1 = temp1 + "_" + temp[i+1]

            data[each_data] = temp1
    return (data)
