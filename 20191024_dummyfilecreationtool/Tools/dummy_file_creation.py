#!/usr/bin/python3
# -*- coding: utf-8 -*-
#File Name: dummy_file_creation.py

#===================================== Revision history ================================
#=======================================================================================
#
#   UPDATE HISTORY     DATE        AUTHOR          MODIFIED POINT
#       Creation    2019.05.15  Mac Tien Truong     Create new
#       Update      2019.07.16  Mac Tien Truong     Replaced access data via index of sheet by name of sheet.

#This program is the dummy_file_creation tool
#Inport the package(s) here:
import os
import xlrd
import plib.dplib

#======================== Get the ASIL Item List from the I/F document =================
#=======================================================================================
def getasilitemlist(sheet_name, row_title_number, list_column):
    "This function is used to get the list of ASIL items from I/F document"
    "Note: Item is either Label or callback function"

    #Define the local variable(s) here
    #Input:
    d_bsw_input_folder = plib.dplib.common_infor.bsw_input_folder
    d_bsw_first_char_name = plib.dplib.common_infor.bsw_first_char_name
    d_bsw_file_name_exten = plib.dplib.common_infor.bsw_file_name_exten
    d_bsw_asil_symbol = plib.dplib.common_infor.bsw_asil_symbol

    #Common:
    d_bsw_sheet_name = sheet_name
    d_bsw_row_title_number = row_title_number
    d_list_column = list_column
    d_list_files = ["NULL"]
    d_asil_list_files = ["NULL"]
    d_received_data = ["NULL"]

    #Step 1: Get the list of the I/F document files in the dedicated folder according the given extension name
    #and the first character of the name file that matches to the current system
    d_list_files_temp = plib.dplib.common.getfilelist(d_bsw_input_folder, d_bsw_file_name_exten)
    for each_file in range(len(d_list_files_temp)):
        if(d_list_files_temp[each_file][0] == d_bsw_first_char_name):
            d_list_files.append(d_list_files_temp[each_file])

    #Remove the first element that is NULL
    if(0 != len(d_list_files)):
        del d_list_files[0]

    #Step 2: Select the ASIL files then add them into the list of ASIL files
    for each_file in range(len(d_list_files)):
        if(-1 != d_list_files[each_file].find(d_bsw_asil_symbol)):
            d_asil_list_files.append(d_list_files[each_file])

    #Remove the first element that is NULL
    if(len(d_asil_list_files) != 0):
        del d_asil_list_files[0]

    #Step 3: Fill ASIL item into received_data list
    for each_col in range(len(d_list_column)):
        for each_file in range(len(d_asil_list_files)):
            d_data = plib.dplib.excel_file_process.getdatafromexcelfiles(d_bsw_input_folder + "/" +\
                                                                         d_asil_list_files[each_file], \
                                                                         d_bsw_sheet_name, \
                                                                         d_list_column[each_col], \
                                                                         d_bsw_row_title_number)
            for each_data in d_data:
                d_received_data.append(each_data)

    #Remove the first element that is NULL
    if(len(d_received_data) != 0):
        del d_received_data[0]

    return(d_received_data)

#======== Get the Data Type for the corresponding label by using dictionary format =====
#======== Label is the key and it's data type is the corresponding value ===============
#=======================================================================================
def getlistdatatypeoflabel():
    "This function is used to get the data type of the label in dictionary format"
    "Key is the label and value is the Data Type"

    #Define the local variable(s) here
    #Input:
    d_bsw_input_folder = plib.dplib.common_infor.bsw_input_folder
    d_bsw_first_char_name = plib.dplib.common_infor.bsw_first_char_name
    d_bsw_file_name_exten = plib.dplib.common_infor.bsw_file_name_exten
    d_bsw_data_type_sheet_name = plib.dplib.common_infor.bsw_data_type_sheet_name
    d_bsw_data_type_row_title = plib.dplib.common_infor.bsw_data_type_row_title
    d_bsw_data_type_label_col_name = plib.dplib.common_infor.bsw_data_type_label_col_name
    d_bsw_data_type_col_name = plib.dplib.common_infor.bsw_data_type_col_name

    #Common:
    d_list_files = ["NULL"]
    d_list_label = ["NULL"]
    d_list_data_type = ["NULL"]
    d_dic_data_type = {"key_is_label": " value_is_data_type"}

    #Step 1: Get the list of the I/F document files in the dedicated folder according the given extension name
    #and the first character of file name that matches to current system
    d_list_files_temp = plib.dplib.common.getfilelist(d_bsw_input_folder, d_bsw_file_name_exten)
    for each_file in range(len(d_list_files_temp)):
        if(d_list_files_temp[each_file][0] == d_bsw_first_char_name):
            d_list_files.append(d_list_files_temp[each_file])

    #Remove the first element that is NULL value
    if(0 != len(d_list_files)):
        del d_list_files[0]

    #Step 2: Get the "Label Name" and the "Data Type" from list of received files
    for each_file in range(len(d_list_files)):
        #For the Label:
        for each_col in d_bsw_data_type_label_col_name:
            d_label_data = plib.dplib.excel_file_process.getdatafromexcelfiles(d_bsw_input_folder + "/" + \
                                                                               d_list_files[each_file], \
                                                                               d_bsw_data_type_sheet_name, \
                                                                               each_col, \
                                                                               d_bsw_data_type_row_title)
            for each_label_data in d_label_data:
                d_list_label.append(each_label_data)

        #For the Data Type:
        for each_col in d_bsw_data_type_col_name:
            d_type_data = plib.dplib.excel_file_process.getdatafromexcelfiles(d_bsw_input_folder + "/" + \
                                                                              d_list_files[each_file], \
                                                                              d_bsw_data_type_sheet_name, \
                                                                              each_col, \
                                                                              d_bsw_data_type_row_title)
            for each_label_data in d_type_data:
                d_list_data_type.append(each_label_data)

    #Remove the first element that is NULL
    if (0 != len(d_list_label)):
        del d_list_label[0]
    if (0 != len(d_list_data_type)):
        del d_list_data_type[0]

    #Remove the row that does not relate to received data
    count  = 0
    while(count < d_bsw_data_type_row_title):
        if (0 != len(d_list_label)):
            del d_list_label[0]
        if (0 != len(d_list_data_type)):
            del d_list_data_type[0]
        count = count + 1

    #Step 3: Creating the dictionary for the "Label Name" and it's Data Type
    #"Label Name" is the key and it's Data Type is the corresponding value
    if (len(d_list_label) == len(d_list_data_type)):
        for each_label in range(len(d_list_label)):
            if(d_list_data_type[each_label] == ""):
                d_list_data_type[each_label] = "float"
            if(d_list_data_type[each_label] == "boolean"):
                d_list_data_type[each_label] = "Bool"
            temp = {d_list_label[each_label]: d_list_data_type[each_label]}
            d_dic_data_type.update(temp)

    #Delete element that has key is ""
    count = 0
    for each_key in d_dic_data_type.keys():
        if (each_key == ""):
            count = count + 1
    while(0 < count):
        del d_dic_data_type[""]
        count = count - 1

    return(d_dic_data_type)


#======== Get the Data size for the corresponding label by using dictionary format =====
#======== Label is the key and it's data size is the corresponding value ===============
#=======================================================================================
def getlistdatasizeoflabel():
    "This function is used to get the data size of the label in dictionary format"
    "Key is the label and value is the Data size"

    #Define the local variable(s) here
    #Input:
    d_bsw_input_folder = plib.dplib.common_infor.bsw_input_folder
    d_bsw_first_char_name = plib.dplib.common_infor.bsw_first_char_name
    d_bsw_file_name_exten = plib.dplib.common_infor.bsw_file_name_exten
    d_bsw_data_type_sheet_name = plib.dplib.common_infor.bsw_data_type_sheet_name
    d_bsw_data_type_row_title = plib.dplib.common_infor.bsw_data_type_row_title
    d_bsw_data_type_label_col_name = plib.dplib.common_infor.bsw_data_type_label_col_name
    d_bsw_data_size_col_name = plib.dplib.common_infor.bsw_data_size_col_name

    #Common:
    d_list_files = ["NULL"]
    d_list_label = ["NULL"]
    d_list_data_size = ["NULL"]
    d_dic_data_size = {"key_is_label": " value_is_data_size"}

    #Step 1: Get the list of the I/F document files in the dedicated folder according the given extension name
    #and the first character of file name that matches to current system
    d_list_files_temp = plib.dplib.common.getfilelist(d_bsw_input_folder, d_bsw_file_name_exten)
    for each_file in range(len(d_list_files_temp)):
        if(d_list_files_temp[each_file][0] == d_bsw_first_char_name):
            d_list_files.append(d_list_files_temp[each_file])

    #Remove the first element that is NULL value
    if(0 != len(d_list_files)):
        del d_list_files[0]

    #Step 2: Get the "Label Name" and the "Data size" from list of received files
    for each_file in range(len(d_list_files)):
        #For the Label:
        for each_col in d_bsw_data_type_label_col_name:
            d_label_data = plib.dplib.excel_file_process.getdatafromexcelfiles(d_bsw_input_folder + "/" + \
                                                                               d_list_files[each_file], \
                                                                               d_bsw_data_type_sheet_name, \
                                                                               each_col, \
                                                                               d_bsw_data_type_row_title)
            for each_label_data in d_label_data:
                d_list_label.append(each_label_data)

        #For the Data size:
        for each_col in d_bsw_data_size_col_name:
            d_data_size = plib.dplib.excel_file_process.getdatafromexcelfiles(d_bsw_input_folder + "/" + \
                                                                              d_list_files[each_file], \
                                                                              d_bsw_data_type_sheet_name, \
                                                                              each_col, \
                                                                              d_bsw_data_type_row_title)
            for each_data_size in d_data_size:
                d_list_data_size.append(each_data_size)

    #Remove the first element that is NULL
    if (0 != len(d_list_label)):
        del d_list_label[0]
    if (0 != len(d_list_data_size)):
        del d_list_data_size[0]

    #Remove the row that does not relate to received data
    count  = 0
    while(count < d_bsw_data_type_row_title):
        if (0 != len(d_list_label)):
            del d_list_label[0]
        if (0 != len(d_list_data_size)):
            del d_list_data_size[0]
        count = count + 1

    #Step 3: Creating the dictionary for the "Label Name" and it's Data Type
    #"Label Name" is the key and it's Data Type is the corresponding value
    if (len(d_list_label) == len(d_list_data_size)):
        for each_label in range(len(d_list_label)):
            if(d_list_data_size[each_label] == ""):
                d_list_data_size[each_label] = 124
            temp = {d_list_label[each_label]: d_list_data_size[each_label]}
            d_dic_data_size.update(temp)

    #Delete element that has key is ""
    count = 0
    for each_key in d_dic_data_size.keys():
        if (each_key == ""):
            count = count + 1
    while(0 < count):
        del d_dic_data_size[""]
        count = count - 1

    return(d_dic_data_size)

#========================== Create the dummy NG label code files =======================
#=======================================================================================
def dummylabelcreation():
    "This function is used to create the dummy NG label code files"
    print("==================== Create the dummy NG label code files ======================")
    print("================================================================================")

    #Define the local variable(s) here
    #Input:
    #For log file(s)
    d_NG_input_folder_lb = plib.dplib.common_infor.NG_input_folder_lb
    d_NG_file_name_ext_lb = plib.dplib.common_infor.NG_file_name_ext_lb
    d_NG_sepa_symbol_lb = plib.dplib.common_infor.NG_sepa_symbol_lb
    d_NG_title_row_number_lb = plib.dplib.common_infor.NG_title_row_number_lb

    #For the BSW excel file(s)
    d_bsw_data_type_sheet_name = plib.dplib.common_infor.bsw_data_type_sheet_name
    d_bsw_data_type_row_title = plib.dplib.common_infor.bsw_data_type_row_title
    d_bsw_list_column_lb = plib.dplib.common_infor.bsw_data_type_label_col_name

    #Output:
    d_NG_output_folder_lb = plib.dplib.common_infor.NG_output_folder_lb
    d_NG_source_file_name_lb = plib.dplib.common_infor.NG_source_file_name_lb
    d_NG_header_file_name_lb = plib.dplib.common_infor.NG_header_file_name_lb

    #Common:
    d_indicator = -1
    d_NG_label_list = ["NULL"]
    d_NG_asil_label_list = ["NULL"]
    d_NG_qm_label_list = ["NULL"]
    d_log_file_list = ["NULL"]

    #Step 1: Get the ASIL label list from I/F document
    d_asil_label_list = getasilitemlist(d_bsw_data_type_sheet_name, d_bsw_data_type_row_title, \
                                        d_bsw_list_column_lb)

    #Step 2: Get the NG label log file(s) in the dedicated folder
    print("List of log file for NG label:")
    d_log_file_list_temp = plib.dplib.common.getfilelist(d_NG_input_folder_lb, \
                                                         d_NG_file_name_ext_lb)
    for each_file in d_log_file_list_temp:
        if(each_file.find("_LABEL_NG_LIST") != -1):
            d_log_file_list.append(each_file)

    del d_log_file_list[0]
    for each_file in d_log_file_list:
        print(each_file)

    #Step 3: Get the list of the NG label from the log file(s)
    for each_file in d_log_file_list:
        d_label_list = plib.dplib.text_file_process.getdatafromtextfile(d_NG_input_folder_lb + \
                                                                        "/" + each_file, \
                                                                        d_NG_title_row_number_lb, \
                                                                        d_NG_sepa_symbol_lb, \
                                                                        d_indicator)

        for each_label in d_label_list:
            d_NG_label_list.append(each_label)

    #Remove the "\n" symbol in the end of the label if have
    for each_label in range(len(d_NG_label_list)):
        d_temp = d_NG_label_list[each_label].split("\n")[0]
        d_NG_label_list[each_label] = d_temp

    #Remove the first element that is NULL
    if(0 != len(d_NG_label_list)):
        del d_NG_label_list[0]

    #Step 4: Assign NG label into the ASIL NG label list or the QM NG label list
    for each_NG_label in d_NG_label_list:
        d_count = 0
        for each_label in d_asil_label_list:
            if (each_NG_label == each_label):
                d_count = d_count +  1
                break

        if (0 != d_count):
            d_NG_asil_label_list.append(each_NG_label) 
        else:
            d_NG_qm_label_list.append(each_NG_label)

    #Remove the first element that is NULL
    if(0 != len (d_NG_asil_label_list)):
        del d_NG_asil_label_list[0]
    if(0 != len (d_NG_qm_label_list)):
        del d_NG_qm_label_list[0]

    #Step 5: Get the dictionary of the data type corresponding with each label
    d_label_data_type = getlistdatatypeoflabel()
    d_label_data_size = getlistdatasizeoflabel()

    #Step 6: Create the dummy NG label code files
    #Source code files:
    plib.dplib.text_file_process.NGlabelsourcefilecreation(d_NG_output_folder_lb, \
                                                           d_NG_source_file_name_lb[1], \
                                                           d_NG_qm_label_list, \
                                                           d_label_data_type, \
                                                           d_label_data_size, \
                                                           "No")
    plib.dplib.text_file_process.NGlabelsourcefilecreation(d_NG_output_folder_lb, \
                                                           d_NG_source_file_name_lb[0], \
                                                           d_NG_asil_label_list, \
                                                           d_label_data_type, \
                                                           d_label_data_size, \
                                                           "Yes")
    #Header code files:
    plib.dplib.text_file_process.NGlabelheaderfilecreation(d_NG_output_folder_lb, \
                                                           d_NG_header_file_name_lb[1], \
                                                           d_NG_qm_label_list, \
                                                           d_label_data_type,
                                                           d_label_data_size, \
                                                           "No")
    plib.dplib.text_file_process.NGlabelheaderfilecreation(d_NG_output_folder_lb, \
                                                           d_NG_header_file_name_lb[0], \
                                                           d_NG_asil_label_list, \
                                                           d_label_data_type,
                                                           d_label_data_size, \
                                                           "Yes")

    return()

#======================= Create the dummy NG callback function code files ==============
#=======================================================================================
def dummycallbackcreation():
    "This function is used to create the dummy NG callback function code files"
    print("============== Create the dummy NG callback function code files ================ ")
    print("================================================================================ ")

    #Define the local variable(s) here
    #Input:
    #For the log file
    d_NG_input_folder_cb = plib.dplib.common_infor.NG_input_folder_cb
    d_NG_file_name_ext_cb = plib.dplib.common_infor.NG_file_name_ext_cb
    d_NG_sepa_symbol_cb = plib.dplib.common_infor.NG_sepa_symbol_cb
    d_NG_title_row_number_cb = plib.dplib.common_infor.NG_title_row_number_cb

    #For the BSW excel file(s)
    d_bsw_data_type_sheet_name = plib.dplib.common_infor.bsw_sheet_name
    d_bsw_list_column_cb = plib.dplib.common_infor.bsw_list_column_cb
    d_bsw_data_type_row_title = plib.dplib.common_infor.bsw_row_title_number

    #Output:
    d_NG_output_folder_cb = plib.dplib.common_infor.NG_output_folder_cb
    d_NG_source_file_name_cb = plib.dplib.common_infor.NG_source_file_name_cb
    d_NG_header_file_name_cb = plib.dplib.common_infor.NG_header_file_name_cb

    #Common:
    d_indicator = -1
    d_NG_callback_list = ["NULL"]
    d_NG_asil_callback_list = ["NULL"]
    d_NG_qm_callback_list = ["NULL"]
    d_log_file_list = ["NULL"]

    #Step 1: Get the ASIL callback function list from I/F document
    d_asil_callback_list = getasilitemlist(d_bsw_data_type_sheet_name, d_bsw_data_type_row_title, \
                                           d_bsw_list_column_cb)

    #Step 2 Get the log file(s) in the dedicated folder
    print("List of log file(s) for NG callback function: ")
    d_log_file_list_temp = plib.dplib.common.getfilelist(d_NG_input_folder_cb, d_NG_file_name_ext_cb)
    for each_file in d_log_file_list_temp:
        if(each_file.find("_CALLBACK_NG_LIST") != -1):
            d_log_file_list.append(each_file)

    del d_log_file_list[0]
    for each_file in d_log_file_list:
        print(each_file)

    #Step 3: Get list of the NG callback function from log file(s)
    for each_file in d_log_file_list:
        d_callback_list = plib.dplib.text_file_process.getdatafromtextfile(d_NG_input_folder_cb + \
                                                                           "/" + each_file, \
                                                                           d_NG_title_row_number_cb, \
                                                                           d_NG_sepa_symbol_cb, \
                                                                           d_indicator)

        for each_callback in d_callback_list:
            d_NG_callback_list.append(each_callback)

    #Remove the "\n" symbol in the end of the callback function if have
    for each_callback in range(len(d_NG_callback_list)):
        d_temp = d_NG_callback_list[each_callback].split("\n")[0]
        d_NG_callback_list[each_callback] = d_temp

    #Remove the first element that is NULL
    if(0 != len(d_NG_callback_list)):
        del d_NG_callback_list[0]

    #Step 4: Assign the NG callback function into ASIL NG callback function list or QM NG callback function list
    for each_NG_callback in d_NG_callback_list:
        d_count = 0
        for each_callback in d_asil_callback_list:
            if (each_NG_callback == each_callback):
                d_count = d_count +  1
                break
        if (0 != d_count):
           d_NG_asil_callback_list.append(each_NG_callback) 
        else:
            d_NG_qm_callback_list.append(each_NG_callback)

    #Remove the first element that is NULL
    if(0 != len (d_NG_asil_callback_list)):
        del d_NG_asil_callback_list[0]
    if(0 != len (d_NG_qm_callback_list)):
        del d_NG_qm_callback_list[0]

    #Step 5: Create the dummy NG callback function code files
    #Source code files:
    plib.dplib.text_file_process.NGcallbacksourcefilecreation(d_NG_output_folder_cb, \
                                                              d_NG_source_file_name_cb[1], \
                                                              d_NG_qm_callback_list, \
                                                              "No")
    plib.dplib.text_file_process.NGcallbacksourcefilecreation(d_NG_output_folder_cb, \
                                                              d_NG_source_file_name_cb[0], \
                                                              d_NG_asil_callback_list, \
                                                              "Yes")
    #Header code files:
    plib.dplib.text_file_process.NGcallbackheaderfilecreation(d_NG_output_folder_cb, \
                                                              d_NG_header_file_name_cb[1], \
                                                              d_NG_qm_callback_list, \
                                                              "No")
    plib.dplib.text_file_process.NGcallbackheaderfilecreation(d_NG_output_folder_cb, \
                                                              d_NG_header_file_name_cb[0], \
                                                              d_NG_asil_callback_list, \
                                                              "Yes")

    return()

#====================================== Main function ==================================
#=======================================================================================  
def main():
    """This function shall generate all the dummy NG label/dummy NG callback
    function code files"""

    dummylabelcreation()
    dummycallbackcreation()
    #plib.dplib.text_file_process.convert_ending_line_format("Yes")
    plib.dplib.text_file_process.convert_ending_line_format("No")
    return()

#==================================== The start of point ===============================
#=======================================================================================
main()
