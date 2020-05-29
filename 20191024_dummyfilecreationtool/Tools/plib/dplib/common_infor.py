#!/usr/bin/python3
# -*- coding: utf-8 -*-
#File Name: common_infor.py

#===================================== Revision history ================================
#=======================================================================================
#
#   UPDATE HISTORY     DATE        AUTHOR          MODIFIED POINT
#       Creation    2019.05.15  Mac Tien Truong     Create new
#       Update      2019.07.16  Mac Tien Truong     Replaced access data via index of sheet by name of sheet.

#This module is used to define the common input/outpout parameters according each system.
#=========== Part 1: Define the input/output parameters for NG dummy code files ========
#========================= For the NG callback function list ===========================
#Input:
NG_input_folder_cb = "../OutputFiles/NG_callback_list"
NG_file_name_ext_cb = "log"
NG_sepa_symbol_cb = ": "                                               #Note: It is TAB symbol
NG_title_row_number_cb = 0

#Output
NG_output_folder_cb = "../OutputFiles/dummy/NG_callback_list"           #The path of the folder stored output files
NG_source_file_name_cb = ["DUMMY_Com_Cbk_SM.c", "DUMMY_Com_Cbk.c"]      #0 for ASIL and 1 for QM
NG_header_file_name_cb = ["DUMMY_Com_Cbk_SM.h", "DUMMY_Com_Cbk.h"]      #0 for ASIL and 1 for QM

#=========================== For the NG label list =====================================
#Input:
NG_input_folder_lb = "../OutputFiles/NG_label_list"
NG_file_name_ext_lb = "log"
NG_sepa_symbol_lb = ": "                                                    #Note: It is TAB symbol
NG_title_row_number_lb = 0

#Output
NG_output_folder_lb = "../OutputFiles/dummy/NG_label_list"                   #The path of the folder stored output files
NG_source_file_name_lb = ["DUMMY_ASW_LABEL_SM.c", "DUMMY_ASW_LABEL.c"]       #0 for ASIL and 1 for QM
NG_header_file_name_lb = ["DUMMY_ASW_LABEL_SM.h", "DUMMY_ASW_LABEL.h"]       #0 for ASIL and 1 for QM


#common
#These parameters are using to create the code dummy files
callback_notification = ["APP合体時にこのファイルは削除してください"]
header_file_list =  ["../../../../../../APPFW_ASIL/app_header_ASIL.h", \
                     "Can_MemMap.h", \
                     "header.h", \
                     "Bsw_Header.h", \
                     "app_callback_header.h", \
                     "Com_Private_def.h", \
                     "../../../../../../APPFW_ASIL/app_callback_header_ASIL.h", \
                     "../../../../APPFW/app_header.h"]

prefix_pragma = ["ASW_SECTION_ASIL", "BSW_SECTION_CAN_ASIL"]
list_pragma = ["_BSS", "_DATA", "_TEXT"]

#========== Part 2: Define the input/output parameters relate to BSW files =============
#=======================================================================================
bsw_input_folder = "../InputFiles/BSW_doc"                                  #The path of the folder stored input files
bsw_first_char_name = "B"                                                   #The first character of the name input files
bsw_file_name_exten = "xlsx"                                                #The name extension of the input files
bsw_sheet_name = "ECM"                                                      #Index of the sheet that we need to get data
bsw_row_title_number = 0                                                    #The row contains the title of the table
bsw_asil_symbol = "B09596"                                                  #Sysbol ASIL in input name file
bsw_list_column_cb = ["Com_CbkCounterErr", "Com_CbkInv", "Com_CbkRxAck"]    #Columns need to get data
bsw_asil_convert_cb = ["vMO_CM_CLCK_ERR_CTR", "vMO_CM_INV_CTR", \
                       "vMO_CM_RX_ACK_CTR"]                                 #0 for Com_CbkCounterErr, 1 for Com_CbkInv and 2 for Com_CbkRxAck
bsw_qm_convert_cb = ["vCLCK_ERR_CTR", "vINV_CTR", \
                     "vRX_ACK_CTR"]                                         #0 for Com_CbkCounterErr, 1 for Com_CbkInv and 2 for Com_CbkRxAck

#These parameters are using to get the data type of label
bsw_data_type_sheet_name = "RAM"                                            #Index of sheet that includes the Data Type of label
bsw_data_type_row_title = 1                                                 #Number of row that includes the title of table
bsw_data_type_label_col_name = ["LabelName"]                                #Column's name that includes the Label name
bsw_data_type_col_name = ["DataType"]                                       #Column's name that includes the Data Type
bsw_data_size_col_name = ["Dimension"]                                      #Column's name that includes the Data Type
