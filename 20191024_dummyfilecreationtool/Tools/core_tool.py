#!/usr/bin/python
# -*- coding: utf-8 -*-
#File Name: core_tool.py

#===================================== Revision history ================================
#=======================================================================================
#
#   UPDATE HISTORY     DATE        AUTHOR          MODIFIED POINT
#       Creation    2019.05.17  Mac Tien Truong     Create new

#This program is the core_tool
#Inport the package(s) here:
import os
import plib.cplib

#Define the global variable(s) here
asw_file_list_dic_lb = {"index": "file_name"}
asw_file_list_dic_cb = {"index": "file_name"}

#=========================== Get the data from the asw document ========================
#=======================================================================================
def getASWdatalist(is_label):
    "This function is used to get data from asw document"

    #Define the local variable(s) here
    #For the label:
    c_asw_input_folder_lb = plib.cplib.common_infor.asw_input_folder_lb
    c_file_type_lb = plib.cplib.common_infor.file_type_lb

    #For thw callback function:
    c_asw_input_folder_cb = plib.cplib.common_infor.asw_input_folder_cb
    c_file_type_cb = plib.cplib.common_infor.file_type_cb

    #Common:
    c_is_label = is_label
    c_asw_data = ["None"]

    #Step 1: Get the list of the asw files
    if (c_is_label == "True"):
        c_asw_file_list = plib.cplib.common.getfilelist(c_asw_input_folder_lb, c_file_type_lb)
    else:
        c_asw_file_list = plib.cplib.common.getfilelist(c_asw_input_folder_cb, c_file_type_cb)

    #Step 2: Get the data from the list of asw files 
    for c_each_file in range(len(c_asw_file_list)):
        if (c_is_label == "True"):
            c_file_name_temp = c_asw_input_folder_lb + "/" + c_asw_file_list[c_each_file]
            asw_file_list_dic_lb.update({c_each_file: c_file_name_temp})
        else:
            c_file_name_temp = c_asw_input_folder_cb + "/" + c_asw_file_list[c_each_file]
            asw_file_list_dic_cb.update({c_each_file: c_file_name_temp})
        
        c_data_temp = plib.cplib.text_file_process.readtextfile(c_file_name_temp)
        for c_index, c_value  in enumerate(c_data_temp):
            c_temp = f'{c_index + 1}:{c_value};  {c_each_file}'
            c_asw_data.append(c_temp)

    del c_asw_data[0]
    
    return (c_asw_data)

#=================================== The NG file creation ==============================
#=======================================================================================
def NGoutputfilecreation(filename, data):
    "This function is used to create the NG output file"

    #Define the local variable(s) here
    l_filename = filename
    l_data = "NG: " + data
    l_write_mode = "a+"

    plib.cplib.text_file_process.writetextfile(l_filename, l_write_mode, l_data + "\n")

    return()

#=================================== The Output file creation ==========================
#=======================================================================================
def OKoutputfilecreation(filename, bsw_data, asw_data, file_dic):
    "This function is used to create the output file"

    #Define the local variable(s) here
    l_filename = filename
    l_file_dic = file_dic
    l_write_mode = "a+"
    l_bsw_data = bsw_data
    l_asw_file_index = int(asw_data.split(";")[-1])
    l_asw_line_index = asw_data.split(":")[0]
    l_asw_data = asw_data.split(";")[0]
    l_asw_data = l_asw_data.split(":")[-1]
    l_tab = "   "

    l_data_write = "OK: " + l_bsw_data + l_tab + l_tab + l_file_dic.setdefault(l_asw_file_index, "None") + \
                          l_tab + l_asw_line_index + ":" + l_asw_data + "\n"
    plib.cplib.text_file_process.writetextfile(l_filename, l_write_mode, l_data_write)

    return()

#============================== Get the data from the bsw document =====================
#=======================================================================================
def getBSWdatalist(is_label):
    "This function use to get the data from the bsw document"

    #Define the local variable(s) here
    #For the label:
    c_bsw_input_folder_lb = plib.cplib.common_infor.bsw_input_folder_lb
    c_file_type_lb = plib.cplib.common_infor.file_type_lb

    #For the callback function:
    c_bsw_input_folder_cb = plib.cplib.common_infor.bsw_input_folder_cb
    c_file_type_cb = plib.cplib.common_infor.file_type_cb

    #Common
    c_is_label = is_label
    c_bsw_data = ["None"]

    #Step 1: Get the list of the bsw files
    if (c_is_label == "True"):
        c_bsw_file_list = plib.cplib.common.getfilelist(c_bsw_input_folder_lb, c_file_type_lb)
    else:
        c_bsw_file_list = plib.cplib.common.getfilelist(c_bsw_input_folder_cb, c_file_type_cb)

    #Step 2: Get the data from the list of asw files 
    for c_each_file in range(len(c_bsw_file_list)):
        if (c_is_label == "True"):
            c_file_name_temp = c_bsw_input_folder_lb + "/" + c_bsw_file_list[c_each_file]
        else:
            c_file_name_temp = c_bsw_input_folder_cb + "/" + c_bsw_file_list[c_each_file]

        #Get the data
        c_data_temp = plib.cplib.text_file_process.readtextfile(c_file_name_temp)
        for each_data in c_data_temp:
            c_bsw_data.append(each_data)

    del c_bsw_data[0]

    return (c_bsw_data)

#================================ Label/Callback function checking =====================
#=======================================================================================
def checkdata(is_label):
    "This function is used to check the label/callback function"

    #Define the local variable(s) here
    #For the label:
    l_NG_out_folder_lb = plib.cplib.common_infor.NG_out_folder_lb
    l_OK_out_file_lb = plib.cplib.common_infor.OK_out_file_lb
    l_NG_out_file_lb = l_OK_out_file_lb + "log_LABEL_NG_LIST.log"

    #For the callback function:
    l_NG_out_folder_cb = plib.cplib.common_infor.NG_out_folder_cb
    l_OK_out_file_cb = plib.cplib.common_infor.OK_out_file_cb
    l_NG_out_file_cb = l_OK_out_file_cb + "_CALLBACK_NG_LIST.log"

    #Common
    c_is_label = is_label

    #Step 1: Creat Output folder ad reset histoty data
    if (c_is_label == "True"):
        plib.cplib.common.makedir(l_NG_out_folder_lb)
        plib.cplib.text_file_process.deletetextfile(l_NG_out_folder_lb + "/" + l_OK_out_file_lb)
        plib.cplib.text_file_process.deletetextfile(l_NG_out_folder_lb + "/" + l_NG_out_file_lb)
        plib.cplib.text_file_process.writetextfile(l_NG_out_folder_lb + "/" + l_OK_out_file_lb, "a+", "")
        plib.cplib.text_file_process.writetextfile(l_NG_out_folder_lb + "/" + l_NG_out_file_lb, "a+", "")
    else:
        plib.cplib.common.makedir(l_NG_out_folder_cb)
        plib.cplib.text_file_process.deletetextfile(l_NG_out_folder_cb + "/" + l_OK_out_file_cb)
        plib.cplib.text_file_process.deletetextfile(l_NG_out_folder_cb + "/" + l_NG_out_file_cb)
        plib.cplib.text_file_process.writetextfile(l_NG_out_folder_cb + "/" + l_OK_out_file_cb, "a+", "")
        plib.cplib.text_file_process.writetextfile(l_NG_out_folder_cb + "/" + l_NG_out_file_cb, "a+", "")

    #Setp 2: Get the data from the ASW document and the BSW document
    c_bsw_data_list = getBSWdatalist(is_label)
    c_asw_data_list = getASWdatalist(is_label)
    if (c_is_label == "True"):
        for each_bsw_data in c_bsw_data_list:
            count = 0
            for each_asw_data in c_asw_data_list:
                temp_data = each_asw_data.split(";")[0]
                temp_data1 = temp_data.split(":")[-1]
                if (temp_data1 == each_bsw_data):
                    count = 1
                    break

            if (count == 1):
                OKoutputfilecreation(l_NG_out_folder_lb + "/" + l_OK_out_file_lb, \
                                     each_bsw_data, \
                                     each_asw_data, \
                                     asw_file_list_dic_lb)
            else:
                NGoutputfilecreation(l_NG_out_folder_lb + "/" + l_OK_out_file_lb, \
                                     each_bsw_data)
                NGoutputfilecreation(l_NG_out_folder_lb + "/" + l_NG_out_file_lb, \
                                     each_bsw_data)
    else:
        for each_bsw_data in c_bsw_data_list:
            count = 0
            for each_asw_data in c_asw_data_list:
                temp_data = each_asw_data.split(";")[0]
                temp_data1 = temp_data.split(":")[-1]
                if (temp_data1.find(each_bsw_data) != -1):
                    count = 1
                    break

            if (count == 1):
                OKoutputfilecreation(l_NG_out_folder_cb + "/" + l_OK_out_file_cb, \
                                     each_bsw_data, \
                                     each_asw_data, \
                                     asw_file_list_dic_cb)
            else:
                NGoutputfilecreation(l_NG_out_folder_cb + "/" + l_OK_out_file_cb, \
                                     each_bsw_data)
                NGoutputfilecreation(l_NG_out_folder_cb + "/" + l_NG_out_file_cb, \
                                     each_bsw_data)
    return()

#====================================== Main function ==================================
#=======================================================================================
def main():
    "This is the main function"
    print("=========================== Start the label checking ===========================")
    checkdata("True")
    print("======================= Start the Callback function checking ===================")
    checkdata("False")

    return()

#==================================== The start of point ===============================
#=======================================================================================
main()
