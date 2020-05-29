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

#========================== Create the folder if it is not existed =====================
#=======================================================================================
def makedir(dir_paths):
    """This sub-function is used to create a list of folder in give path if has any
    foler that is not existed"""

    #Define the local variable(s) here:
    l_dir_paths = dir_paths

    #Procedure to create the list of folders
    l_list_dirs = l_dir_paths.split("/")
    l_edit_dir = l_list_dirs[0]
    #In the first folder, checking if it is not existed then create it
    if(not(os.path.exists(l_edit_dir))):
        os.mkdir(l_edit_dir)

    #Step by step for the ramaining folder(s) in the give dir_paths
    count = 1
    while(count < len(l_list_dirs)):
        l_edit_dir = l_edit_dir + "/" + l_list_dirs[count]
        #If the folder is not existed then create it
        if(not(os.path.exists(l_edit_dir))):
            os.mkdir(l_edit_dir)
        count = count + 1

    return()

#================== Get all files in selected folder with extension name ===============
#=======================================================================================
def getfilelist(dir_path, file_name_extension):
    """This function is used to get the list of files from given
    folder with the format is identifed by file_name_extension parameter"""

    #Define the local variable(s) here:
    l_dir_path = dir_path
    l_file_name_extension = file_name_extension
    l_list_of_files = ["NULL"]
    count = 0

    #Procedure to get the list of file
    if(os.path.exists(l_dir_path)):
        l_files = os.listdir(l_dir_path)
        for each_file in l_files:
            if(each_file.endswith(l_file_name_extension)):
                l_list_of_files.append(each_file)
                count = count + 1
        if (count > 0):
            del l_list_of_files[0]
        else:
            print("Could not find out the file in the folder", l_dir_path)
    else:
       print("Could not find out the input folder", l_dir_path) 

    return(l_list_of_files)
