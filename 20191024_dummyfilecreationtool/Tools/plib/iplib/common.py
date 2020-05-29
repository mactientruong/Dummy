#!/usr/bin/python3
# -*- coding: utf-8 -*-
#File Name: common.py

#===================================== Revision history ================================
#=======================================================================================
#
#   UPDATE HISTORY     DATE        AUTHOR          MODIFIED POINT
#       Creation    2019.05.15  Mac Tien Truong     Create new

#This module is used to define some common functions.
import os
import xlrd

#========================= Create the folder if it is not existed ======================
#=======================================================================================
def makedir(dirpaths):
    "This function is used to create a list of folder"

    #Procedure to create the list of folders
    listdirs = dirpaths.split("/")
    editdir = listdirs[0]
    if(not(os.path.exists(editdir))):
        os.mkdir(editdir)

    count = 1
    while(count < len(listdirs)):
        editdir = editdir + "/" + listdirs[count]
        #If the folder is not existed then create it
        if(not(os.path.exists(editdir))):
            os.mkdir(editdir)
        count = count + 1
        
    return()

#================== Get all files in selected folder with extension name ===============
#=======================================================================================
def getfilelist(dirpath, extensionname):
    """This function is used to get the list of file from given
    folder with the format is identifed by extensionname"""

    # Local variable(s) are defined here
    listoffile = ["NULL"]
    count = 0
    #Procedure to get the list of file
    if(os.path.exists(dirpath)):
        files = os.listdir(dirpath)
        for each_file in files:
            if(each_file.endswith(extensionname)):
                listoffile.append(each_file)
                count = count + 1
        if (count > 0):
            del listoffile[0]
            #print("Find out the file in the folder")
        else:
            print("Could not find out the file in the folder", dirpath)
    else:
       print("Could not find out the input folder", dirpath) 
    
    return(listoffile)
