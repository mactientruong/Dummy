#!/usr/bin/python3
# -*- coding: utf-8 -*-
#File Name: input_file_creation.py

#===================================== Revision history ================================
#=======================================================================================
#
#   UPDATE HISTORY     DATE        AUTHOR          MODIFIED POINT
#       Creation    2019.05.15  Mac Tien Truong     Create new
#       Update      2019.07.16  Mac Tien Truong     Replaced access data via index of sheet by name of sheet.

#This program is the input_file_creation tool
#Import some packages
import os
import xlrd
import plib.iplib

#========================= Part 1: BSW Callback Function Writing =======================
#=======================================================================================
#function name: bswlistwritingcallback()
def bswlistwritingcallback():
    "This function is used to write the callback function into the BSW callback output file"
    print("===================== Part 1: BSW Callback Function Writing ====================")
    print("================================================================================")

    #Define some local variables here
    #Input:
    input_folder_path_cb = plib.iplib.bsw_common_infomation.bsw_input_folder_path
    first_name_character_cb = plib.iplib.bsw_common_infomation.bsw_first_char_name
    file_name_extension_cb = plib.iplib.bsw_common_infomation.bsw_file_name_extension
    sheet_name_cb = plib.iplib.bsw_common_infomation.bsw_sheet_name
    row_title_cb = plib.iplib.bsw_common_infomation.bsw_row_title_number
    column_name_cb = plib.iplib.bsw_common_infomation.bsw_list_column_cb
    asil_sysbol_cb = plib.iplib.bsw_common_infomation.bsw_asil_symbol
    list_file_cb = ["None"]
    asil_list_file_cb = ["None"]
    qm_list_file_cb = ["None"]

    #Output:
    output_folder_path_cb = plib.iplib.bsw_common_infomation.bsw_output_folder_path_cb
    output_file_name_cb = plib.iplib.bsw_common_infomation.bsw_output_file_name_cb

    #Create the output folder if they are not existed
    plib.iplib.common.makedir(output_folder_path_cb)
    #Reset the BSW callback output file
    for each_file in range(len(output_file_name_cb)):
        plib.iplib.text_file_process.deletetextfile(output_folder_path_cb + "/" + \
                                                    output_file_name_cb[each_file])

    #Get the BSW callback input files with the first character of name that matches system
    list_files = plib.iplib.common.getfilelist(input_folder_path_cb, file_name_extension_cb)
    for each_file in range(len(list_files)):
        if(list_files[each_file][0] == first_name_character_cb):
            list_file_cb.append(list_files[each_file])

    #Remove the first element that is NULL
    if(len(list_file_cb) != 0):
        del list_file_cb[0]

    #Assign the files into ASIL and QM list
    for each_file in range(len(list_file_cb)):
        if(-1 != list_file_cb[each_file].find(asil_sysbol_cb)):
            asil_list_file_cb.append(list_files[each_file])
        else:
            qm_list_file_cb.append(list_files[each_file])

    #Remove the first element that is NULL
    if(len(asil_list_file_cb) != 0):
        del asil_list_file_cb[0]
    if(len(qm_list_file_cb) != 0):
        del qm_list_file_cb[0]

    print("List of ASIL input file")
    for each_file in range(len(asil_list_file_cb)):
        print(asil_list_file_cb[each_file])

    print("List of QM input file")
    for each_file in range(len(qm_list_file_cb)):
        print(qm_list_file_cb[each_file])

    #Write the callback functions of the BSW into ASIL output file
    for each_col in range(len(column_name_cb)):
        for each_file in range(len(asil_list_file_cb)):
            data = plib.iplib.excel_file_process.getdatafromexcelfiles(input_folder_path_cb + \
                                                                       "/" + \
                                                                       asil_list_file_cb[each_file], \
                                                                       sheet_name_cb, \
                                                                       column_name_cb[each_col], \
                                                                       row_title_cb)
            count = 0
            #Remove the rows that is not relate to expected data
            while (count < row_title_cb):
                if(len(data) != 0):
                    del data[0]
                count = count + 1
            #Write callback functions of the BSW into ASIL output file
            for each in range(len(data)):
                if(data[each] != "NULL"):
                    plib.iplib.text_file_process.writetextfile(output_folder_path_cb + "/" + \
                                                               output_file_name_cb[0], "a+", \
                                                               data[each])
                    plib.iplib.text_file_process.writetextfile(output_folder_path_cb + "/" + \
                                                               output_file_name_cb[0], \
                                                               "a+", "\n")

    #Write the callback functions of the BSW into QM output file
    for each_col in range(len(column_name_cb)):
        for each_file in range(len(qm_list_file_cb)):
            data = plib.iplib.excel_file_process.getdatafromexcelfiles(input_folder_path_cb + \
                                                                       "/" + \
                                                                       qm_list_file_cb[each_file], \
                                                                       sheet_name_cb, \
                                                                       column_name_cb[each_col], \
                                                                       row_title_cb)
            count = 0
            #Remove the rows that does not relate to expected data
            while (count < row_title_cb):
                if(len(data) != 0):
                    del data[0]
                count = count + 1
            #Write callback functions of the BSW into QM output file
            for each in range(len(data)):
                if(data[each] != "NULL"):
                    plib.iplib.text_file_process.writetextfile(output_folder_path_cb + \
                                                               "/" + \
                                                               output_file_name_cb[1], \
                                                               "a+", \
                                                               data[each])
                    plib.iplib.text_file_process.writetextfile(output_folder_path_cb + \
                                                               "/" + \
                                                               output_file_name_cb[1], \
                                                               "a+", \
                                                               "\n")

    return()

#================================ Part 2: BSW Labels Writing  ==========================
#=======================================================================================
#function name: bswlistwritinglabels()
def bswlistwritinglabels():
    "This function is used to write the BSW label into the BSW label output file"
    print("======================== Part 2: BSW Labels Writing  ===========================")
    print("================================================================================")

    #Define some local variables here
    #Input:
    input_folder_path_lb = plib.iplib.bsw_common_infomation.bsw_input_folder_path
    first_name_character_lb = plib.iplib.bsw_common_infomation.bsw_first_char_name
    file_name_extecsion_lb = plib.iplib.bsw_common_infomation.bsw_file_name_extension
    sheet_name_lb = plib.iplib.bsw_common_infomation.bsw_sheet_name
    row_title_lb = plib.iplib.bsw_common_infomation.bsw_row_title_number
    column_name_lb = plib.iplib.bsw_common_infomation.bsw_list_column_lb
    ROM_sheet_name = plib.iplib.bsw_common_infomation.bsw_ROM_sheet_name
    ROM_list_column_lb = plib.iplib.bsw_common_infomation.bsw_ROM_list_column_lb
    ROM_row_title_number = plib.iplib.bsw_common_infomation.bsw_ROM_row_title_number
    list_files_lb = ["NULL"]

    #Output:
    output_folder_path_lb = plib.iplib.bsw_common_infomation.bsw_output_folder_path_lb
    output_file_name_lb = plib.iplib.bsw_common_infomation.bsw_output_file_name_lb

    #Common:
    vtx_symbol = "Vtx_"
    RAM_list_lb = ["None"]
    ROM_list_lb = ["None"]

    #Create the output folder if they are not existed
    plib.iplib.common.makedir(output_folder_path_lb)
    #Reset the BSW label output file
    plib.iplib.text_file_process.deletetextfile(output_folder_path_lb + "/" + output_file_name_lb)

    #Get the list of the BSW label output files with the first character of name that matches system
    list_files = plib.iplib.common.getfilelist(input_folder_path_lb, file_name_extecsion_lb)
    for each_file in range(len(list_files)):
        if(list_files[each_file][0] == first_name_character_lb):
            list_files_lb.append(list_files[each_file])

    #Remove the first element that is NULL
    if(len(list_files_lb) != 0):
        del list_files_lb[0]

    print("The list of the BSW label input file")
    for each_file in range(len(list_files_lb)):
        print(list_files_lb[each_file])

    #Get lable from RAM
    for each_col in range(len(column_name_lb)):
        for each_file in range(len(list_files_lb)):
            data = plib.iplib.excel_file_process.getdatafromexcelfiles(input_folder_path_lb + \
                                                                       "/" + \
                                                                       list_files_lb[each_file], \
                                                                       sheet_name_lb, \
                                                                       column_name_lb[each_col], \
                                                                       row_title_lb)
            count = 0
            #Remove the rows that does not relate to expected data
            while (count < row_title_lb):
                if(len(data) != 0):
                    del data[0]
                count = count + 1
            #Get the labels from RAM into the RAM_list_lb
            for each in range(len(data)):
                if((data[each].find(vtx_symbol) == -1) and (data[each] != "NULL")):
                    RAM_list_lb.append(data[each])

    #Remove the first data that is None
    del RAM_list_lb[0]
    for each_col in ROM_list_column_lb:
        for each_file in list_files_lb:
            data = plib.iplib.excel_file_process.getdatafromexcelfiles(input_folder_path_lb + \
                                                                       "/" + \
                                                                       each_file, \
                                                                       ROM_sheet_name, \
                                                                       each_col, \
                                                                       ROM_row_title_number)
            count = 0
            #Remove the rows that does not relate to expected data
            while (count < ROM_row_title_number):
                if(len(data) != 0):
                    del data[0]
                count = count + 1

            #Get lable into ROM_list_lb
            for each_data in data:
                if(each_data != "NULL"):
                    ROM_list_lb.append(each_data)

    #Remove the first data that is None
    del ROM_list_lb[0]
    #Remove the labels that are defined in ROM
    RAM_each_data_index = 0
    while (RAM_each_data_index < len(RAM_list_lb)):
        count = 0
        for each_data in ROM_list_lb:
            if(RAM_list_lb[RAM_each_data_index] == each_data):
                count +=1
                break
        if (count != 0):
            del RAM_list_lb[RAM_each_data_index]
        else:
           RAM_each_data_index += 1

    #Write lable in the output file
    for each_data in RAM_list_lb:
        plib.iplib.text_file_process.writetextfile(output_folder_path_lb + \
                                                   "/" + \
                                                   output_file_name_lb, \
                                                   "a+", \
                                                   each_data.split("[")[0])
        plib.iplib.text_file_process.writetextfile(output_folder_path_lb + \
                                                   "/" + \
                                                   output_file_name_lb, \
                                                   "a+", \
                                                   "\n")
    return()

#============================== Part 3: ASW Labels Writing  ============================
#=======================================================================================
#function name: aswlistwritinglabels()
def aswlistwritinglabels():
    "This function is used to write the ASW label into the ASW label output file"
    print("======================== Part 3: ASW Labels Writing  ===========================")
    print("================================================================================")

    #Define local variables here
    #Input:
    input_folder_path_lb = plib.iplib.asw_common_infomation.asw_input_folder_path_lb
    file_name_extension_lb = plib.iplib.asw_common_infomation.asw_file_name_extension_lb
    sheet_name_lb = plib.iplib.asw_common_infomation.asw_sheet_name_lb
    column_name_lb = plib.iplib.asw_common_infomation.asw_list_column_lb
    row_title_lb = plib.iplib.asw_common_infomation.asw_row_title_number_lb
    split_symbol_lb = plib.iplib.asw_common_infomation.asw_separate_symbol_lb
    ending_symbol_list_lb = plib.iplib.asw_common_infomation.asw_list_end_symbol_lb

    #Output:
    output_folder_path_lb = plib.iplib.asw_common_infomation.asw_output_folder_path_lb
    output_file_name_lb = plib.iplib.asw_common_infomation.asw_output_file_name_lb

    #Create the output folder if they are not existed
    plib.iplib.common.makedir(output_folder_path_lb)
    #Reset the ASW label output file
    plib.iplib.text_file_process.deletetextfile(output_folder_path_lb + "/" + output_file_name_lb)

    #Get the list of ASW label input files
    print("List of the ASW label input files are: ")
    list_xls_files = plib.iplib.common.getfilelist(input_folder_path_lb, file_name_extension_lb)
    for each_file in range(len(list_xls_files)):
        print(list_xls_files[each_file])

    #Write the labels into the ASW output text file
    for each_col in range(len(column_name_lb)):
        for each_file in range(len(list_xls_files)):
            data = plib.iplib.excel_file_process.getdatafromexcelfiles(input_folder_path_lb + \
                                                                       "/" + \
                                                                       list_xls_files[each_file], \
                                                                       sheet_name_lb, \
                                                                       column_name_lb[each_col], \
                                                                       row_title_lb)
            #Remove the rows that does not relate to expected data
            count = 0
            while (count < row_title_lb):
                if(0 != len(data)):
                    del data[0]
                count = count + 1

            #Need to convert the data for some items that have ending symbol is mf or f
            for each_ending in range(len(ending_symbol_list_lb)):
                data_temp = plib.iplib.excel_file_process.convertdata(data, split_symbol_lb, \
                                                                      ending_symbol_list_lb[each_ending])

            #Write symbols into ASW output file
            for each in range(len(data_temp)):
                if(data_temp[each] != "NULL"):
                    plib.iplib.text_file_process.writetextfile(output_folder_path_lb + \
                                                               "/" + \
                                                               output_file_name_lb, \
                                                               "a+", data_temp[each])
                    plib.iplib.text_file_process.writetextfile(output_folder_path_lb + \
                                                               "/" + \
                                                               output_file_name_lb, \
                                                               "a+",\
                                                               "\n")

    return()

#======================== Part 4: ASW Callabck Function Writing  =======================
#=======================================================================================
#function name: aswlistwritingcallback()
def aswlistwritingcallback():
    "This function is used to write the callback function into the ASW callback function output file."
    print("=================== Part 4: ASW Callabck Function Writing  =====================")
    print("================================================================================")

    #Define the local variables here
    #Input:
    input_folder_path_cb = plib.iplib.asw_common_infomation.asw_input_folder_path_cb
    row_title_cb = plib.iplib.asw_common_infomation.asw_row_title_number_cb
    file_name_extension_cb = plib.iplib.asw_common_infomation.asw_file_name_extension_cb
    asil = "_ASIL"
    nonasil = "_QM"
    list_txt_files_asil = ["NULL"]
    list_txt_files_qm = ["NULL"]

    #Output:
    output_folder_path_cb = plib.iplib.asw_common_infomation.asw_output_folder_path_cb
    output_filename_cb = plib.iplib.asw_common_infomation.asw_output_file_name_cb

    #Create the output folder if they are not existed
    plib.iplib.common.makedir(output_folder_path_cb)
    #Reset the output text files to make sure clear all history data
    for each_file in range(len(output_filename_cb)):
        plib.iplib.text_file_process.deletetextfile(output_folder_path_cb + "/" + \
                                                    output_filename_cb[each_file])

    #Get the list of the txt file then assign them into ASIL or QM list
    list_txt_files = plib.iplib.common.getfilelist(input_folder_path_cb, \
                                                   file_name_extension_cb)
    for each_file in range(len(list_txt_files)):
        if (-1 != list_txt_files[each_file].find(asil)):
            list_txt_files_asil.append(list_txt_files[each_file])
        elif (-1 != list_txt_files[each_file].find(nonasil)):
            list_txt_files_qm.append(list_txt_files[each_file])

    #Remove the first element that is NULL
    if(len(list_txt_files_asil) != 0):
        del list_txt_files_asil[0]
    if(len(list_txt_files_qm) != 0):
        del list_txt_files_qm[0]

    #List of ASIL and QM file
    print("List of ASIL input files")
    for each in range(len(list_txt_files_asil)):
        print(list_txt_files_asil[each])

    print("List of QM input files")
    for each in range(len(list_txt_files_qm)):
        print(list_txt_files_qm[each])

    #Write the callback functions into the ASIL output text file
    number_of_file = len(list_txt_files_asil)
    count = 0
    while(count < number_of_file):
        data = plib.iplib.text_file_process.getdatafromtextfile(input_folder_path_cb + \
                                                                "/" + \
                                                                list_txt_files_asil[count], \
                                                                row_title_cb)
        for each in range(len(data)):
            #Write callback functions into the ASIL file
            if(data[each] != "NULL"):
                plib.iplib.text_file_process.writetextfile(output_folder_path_cb + \
                                                           "/" + \
                                                           output_filename_cb[0], \
                                                           "a+", \
                                                           data[each])
        count = count + 1

    #Write the callback functions into the QM output text file
    number_of_file = len(list_txt_files_qm)
    count = 0
    while(count < number_of_file):
        data = plib.iplib.text_file_process.getdatafromtextfile(input_folder_path_cb + \
                                                                "/" + \
                                                                list_txt_files_qm[count], \
                                                                row_title_cb)
        for each in range(len(data)):
            #Write callback functions into the QM file
            if(data[each] != "NULL"):
                plib.iplib.text_file_process.writetextfile(output_folder_path_cb + \
                                                           "/" + \
                                                           output_filename_cb[1], \
                                                           "a+", \
                                                           data[each])
        count = count + 1

    return()

#====================================== Main function ==================================
#=======================================================================================
#function name: main()
def main():
    "This is the main function is used to generate all the expected output files"
    bswlistwritingcallback()
    bswlistwritinglabels()
    aswlistwritinglabels()
    aswlistwritingcallback()

    return()

#==================================== The start of point ===============================
#=======================================================================================
main()
