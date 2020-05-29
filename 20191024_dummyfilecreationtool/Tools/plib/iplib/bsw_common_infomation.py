#!/usr/bin/python3
# -*- coding: utf-8 -*-
#File Name: bsw_common_information.py

#===================================== Revision history ================================
#=======================================================================================
#
#   UPDATE HISTORY     DATE        AUTHOR          MODIFIED POINT
#       Creation    2019.05.15  Mac Tien Truong     Create new
#       Update      2019.07.16  Mac Tien Truong     Replaced access data via index of sheet by name of sheet.

#This module is used to define the bsw common information according the each system.
#===================================== Common ==========================================
bsw_input_folder_path = "../InputFiles/BSW_doc"                              #The path of the folder stored input files
bsw_first_char_name = "B"                                                    #The first character of the name input files
bsw_file_name_extension = "xlsx"                                             #The name extension of the input files
bsw_sheet_name = "ECM"                                                       #Index of the sheet that we need to get data
bsw_row_title_number = 0                                                     #The row contains the title of the table
bsw_asil_symbol = "B09596"                                                   #Sysbol ASIL in input name file
bsw_ROM_sheet_name = "ROM"                                                   #Index of the sheet that we need to get data from ROM

#================================== For the callback function ==========================
bsw_list_column_cb = ["Com_CbkCounterErr", "Com_CbkInv", "Com_CbkRxAck"]      #Columns need to get data
bsw_output_folder_path_cb = "../OutputFiles/BSW_list/BSW_Callback_list"       #The path of the folder stored output files
bsw_output_file_name_cb = ["list_callback_asil_bsw.txt", "list_callback_qm_bsw.txt"] #0 for ASIL and 1 for QM


#==================================== For the label symbols ============================
bsw_list_column_lb = ["Variable EMS Label", "Tx Invalid Boolean Label", \
                      "CRC Check Result Boolean Label", "Tx Enable Boolean Label"]  #Columns need to get data
bsw_output_folder_path_lb = "../OutputFiles/BSW_list/BSW_Label_list"                #The path of the folder stored output files
bsw_output_file_name_lb = "list_label_bsw.txt"
bsw_ROM_list_column_lb = ["LabelName"]
bsw_ROM_row_title_number = 1