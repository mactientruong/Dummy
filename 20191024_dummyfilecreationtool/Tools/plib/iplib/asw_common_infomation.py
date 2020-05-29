#!/usr/bin/python3
# -*- coding: utf-8 -*-
#File Name: asw_common_information.py

#===================================== Revision history ================================
#=======================================================================================
#
#   UPDATE HISTORY     DATE        AUTHOR          MODIFIED POINT
#       Creation    2019.05.15  Mac Tien Truong     Create new
#       Update      2019.07.16  Mac Tien Truong     Replaced access data via index of sheet by name of sheet.

#This module is used to define the asw common information according the each system.
#================================= Common ==============================================

#=========================== For the callback function =================================
asw_input_folder_path_cb = "../InputFiles/ASW_doc/ASW_Callback_doc"            #The path of the folder stored input files
asw_file_name_extension_cb = "txt"                                             #The name extension of the input files
asw_row_title_number_cb = 2                                                    #The row contains the title of the table
asw_output_folder_path_cb = "../OutputFiles/ASW_list/ASW_Callback_list"        #The path of the folder stored output files
asw_output_file_name_cb = ["list_callback_asil_asw.txt", "list_callback_qm_asw.txt"] #0 for asil and 1 for QM

#========================== For the label symbols ======================================
#Input information:
asw_input_folder_path_lb = "../InputFiles/ASW_doc/ASW_Label_doc"               #The path of the folder stored input files
asw_file_name_extension_lb = "xls"                                             #The name extension of the input files
asw_sheet_name_lb = "DDSHEET"                                                  #Index of the sheet that we need to get data
asw_list_column_lb = ["Byte"]                                                  #Columns need to get data
asw_row_title_number_lb = 2                                                    #The row contains the title of the table
asw_separate_symbol_lb = "_"                                                   #The symbol that is used to separate the name
asw_list_end_symbol_lb = ["f", "mf"]                                           #List of ending symbol that need to change format

#Output information:
asw_output_folder_path_lb = "../OutputFiles/ASW_list/ASW_Label_list"           #The path of the folder stored output files
asw_output_file_name_lb = "list_label_asw.txt"
