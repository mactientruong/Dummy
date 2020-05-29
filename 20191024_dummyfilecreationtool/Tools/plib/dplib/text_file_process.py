#!/usr/bin/python3
# -*- coding: utf-8 -*-
#File Name: text_file_process.py

#===================================== Revision history ================================
#=======================================================================================
#
#   UPDATE HISTORY     DATE        AUTHOR          MODIFIED POINT
#       Creation    2019.05.15  Mac Tien Truong     Create new
#       Update      2019.10.24  Mac Tien Truong     Comment line code
#       l_ojb_file.write(l_include + "\"" + l_header_list[6] + "\"" + "\n") in function
#       NGcallbackheaderfilecreation() to remove
#       "include "../../../../../../APPFW_ASIL/app_callback_header_ASIL.h
#       in hearder file DUMMY_Com_Cbk_SM.h
#
#This module is use to define the functions relate to text file process.

import os
import xlrd
from plib.dplib import common
from plib.dplib import common_infor

#========================== Write data into the text file ==============================
#=======================================================================================
def writetextfile(text_file_name, mode_write, data_write):
    "This function is used to write the data in the text file"

    #Define the local variable(s) here
    l_text_file_name = text_file_name
    l_mode_write = mode_write
    l_data_write = data_write

    #Procedure to write the data into the text file
    l_ojb_text_file = open(l_text_file_name, l_mode_write)
    l_ojb_text_file.write(l_data_write)
    l_ojb_text_file.close()

    return()

#========================= Read the data from the text file ============================
#=======================================================================================
def readtextfile(text_file_name):
    "This function is used to read the data from the text file"

    #Define the local variable(s) here
    l_text_file_name = text_file_name

    #Procedure to read a text file
    if (os.path.exists(l_text_file_name)):
        l_obj_text_file = open(l_text_file_name)
        l_received_data = l_obj_text_file.read()
        l_obj_text_file.close()
    else:
        print("Could not find out the file name:", text_file_name)

    return(l_received_data)

#=========================== Get the data from the text file ===========================
#=======================================================================================
def getdatafromtextfile(text_file_name, title_row_number, symbol_sepa, indicator):
    "This function is used to get the data in the text file"

    #Define local variable(s) here
    l_text_file_name = text_file_name
    l_title_row_number = title_row_number
    l_symbol_sepa = symbol_sepa
    l_indicator = indicator
    l_data = ["NULL"]

    #procedure to get the data
    if (os.path.exists(l_text_file_name)):
        l_obj_text_file = open(l_text_file_name)
        l_received_data = l_obj_text_file.readlines()
        l_obj_text_file.close()

        #Extract data from text file
        for each_data in range(len(l_received_data)):
            l_data.append(l_received_data[each_data].split(l_symbol_sepa)[l_indicator])

        if(0 != len(l_data)):
            del l_data[0] #Remove the first element
        count = 0
        while (count < l_title_row_number):
            if (0 != len(l_data)):
                del l_data[0] #Remove the rows that are not related to expected data
            count = count + 1
    else:
        print("Could not find out the file name: ", l_text_file_name)

    return (l_data)

#============================= Delete the text file ====================================
#=======================================================================================
def deletetextfile(text_file_name):
    "This function is used to delete the current text file"

    #Define local variable(s) here
    l_text_file_name = text_file_name

    #Procedure to delete the current text file
    #Check if it is existed then delete else do nothing
    if(os.path.exists(l_text_file_name)):
        os.remove(l_text_file_name)

    return()

#====================== ASIL callback function's variables convert  ====================
#=======================================================================================
def asilvariableconvertcb(callback_list):
    "This function is used to convert the ASIL callback function's variables"

    #Define local variable(s) here
    l_asil_conv_func_list_cb = callback_list
    l_asil_convert_symbol = common_infor.bsw_asil_convert_cb    
    l_count_symbol_cb = "Com_CbkCounterErr"
    l_inv_symbol_cb = "Com_CbkInv"
    l_ack_symbol_cb = "Com_CbkRxAck"
    l_comc = "_COMC"    
    l_asil_conv_var_list_cb = ["NULL"]

    #Procedure to convert here
    for each in l_asil_conv_func_list_cb:
        l_count = 0
        l_temp1 = each.split("_L2")[-1]
        #For the Com_CbkCounterErr functions
        if(each.find(l_count_symbol_cb) != -1):
            l_count =  1
            l_temp2 = l_asil_convert_symbol[0] + l_temp1 + l_comc
        #For the Com_CbkInv functions
        elif (each.find(l_inv_symbol_cb) != -1):
            l_count =  1
            l_temp2 = l_asil_convert_symbol[1] + l_temp1 + l_comc
        #For the Com_CbkRxAck functions
        elif (each.find(l_ack_symbol_cb) != -1):
            l_count =  1
            l_temp2 = l_asil_convert_symbol[2] + l_temp1 + l_comc

        if (l_count ==  1):
            l_asil_conv_var_list_cb.append(l_temp2)

    #Delete the first element that is null value
    if(len(l_asil_conv_var_list_cb) != 0 ):
        del l_asil_conv_var_list_cb[0]

    return(l_asil_conv_var_list_cb)

#======================= QM callback function's variables convert  =====================
#=======================================================================================
def qmvariableconvertcb(callback_list):
    "This function is used to convert the QM callback function's variables"

    #Define local variable(s) here
    l_qm_conv_func_list_cb = callback_list
    l_qm_convert_symbol = common_infor.bsw_qm_convert_cb    
    l_count_symbol_cb = "Com_CbkCounterErr"
    l_inv_symbol_cb = "Com_CbkInv"
    l_ack_symbol_cb = "Com_CbkRxAck"
    l_comc = "_COMC"    
    l_qm_conv_var_list_cb = ["NULL"]

    #Procedure to convert here
    for each in l_qm_conv_func_list_cb:
        l_count = 0
        #For the Com_CbkCounterErr functions
        if(each.find(l_count_symbol_cb) != -1):
            l_count =  1
            l_temp1 = each.split(l_count_symbol_cb)[-1]
            l_temp2 = l_qm_convert_symbol[0] + l_temp1 + l_comc
        #For the Com_CbkInv functions
        elif (each.find(l_inv_symbol_cb) != -1):
            l_count =  1
            l_temp1 = each.split(l_inv_symbol_cb)[-1]
            l_temp2 = l_qm_convert_symbol[1] + l_temp1 + l_comc
        #For the Com_CbkRxAck functions
        elif (each.find(l_ack_symbol_cb) != -1):
            l_count =  1
            l_temp1 = each.split(l_ack_symbol_cb)[-1]
            l_temp2 = l_qm_convert_symbol[2] + l_temp1 + l_comc

        if(l_count ==  1):
            l_qm_conv_var_list_cb.append(l_temp2)

    #Delete the first element that is null value
    if(len(l_qm_conv_var_list_cb) != 0 ):
        del l_qm_conv_var_list_cb[0]

    return(l_qm_conv_var_list_cb)

#========================== Callback function's variables convert  =====================
#=======================================================================================
def variableconvertcb(callback_list, is_asil):
    "This function is used to convert the callback function's variables"

    #Define local variable(s) here
    l_callbacl_list = callback_list
    l_is_asil = is_asil

    #Procedure to convert here
    if(l_is_asil == "Yes"):
        l_convert_symbol_list_cb = asilvariableconvertcb(l_callbacl_list)
    else:
        l_convert_symbol_list_cb = qmvariableconvertcb(l_callbacl_list)

    return(l_convert_symbol_list_cb)

#============== Delete the first charater of each element in the list  =================
#=======================================================================================
def removefirstcharater(array_data):
    "This function is used to delete the first charater of all elements in given list"

    l_data = array_data
    l_new_data = ["NULL"]

    for each_data in l_data:
        l_temp = each_data
        if(len(l_temp) > 2):
            l_temp1 =  l_temp[1]
            count = 2
            while(count < len(l_temp)):
               l_temp1 = l_temp1 +  l_temp[count]
               count = count + 1
        else:
            l_temp1 = ["NULL"]
        
        l_new_data.append(l_temp1)

    del l_new_data[0]

    return(l_new_data)

#================================== Remove the duplicated data =========================
#=======================================================================================
def removeduplicate(data_list):
    "This function is used to remove the duplicated data"

    l_data_list = data_list
    l_count1 = 0
    while (l_count1 < len(l_data_list) - 1):
        l_temp = l_data_list[l_count1]
        l_count2 = l_count1 + 1
        while (l_count2 < len(l_data_list)):
            if(l_temp == l_data_list[l_count2]):
               del l_data_list[l_count2]
            else:
                l_count2 = l_count2 + 1
        l_count1 = l_count1 + 1

    return(l_data_list)

#=== Sort the list by the lenght of each element that is either decrease or increase ===
#=======================================================================================
def sortarray(array_data, dec):
    """This function is used to sort a list by the lenght, each element that is either
    decrease or increase"""

    l_data = array_data
    l_dec = dec
    count1 = 0
    #For decrease:
    if(l_dec == "Yes"):
        while (count1 < (len(l_data) -1)):
            count2 = count1 + 1
            while (count2 < len(l_data)):
                if (len(l_data[count1]) < len(l_data[count2])):
                    temp = l_data[count1]
                    l_data[count1] = l_data[count2]
                    l_data[count2] = temp
                count2 = count2 + 1
            count1 = count1 + 1
    #For increase:
    else:
        while (count1 < (len(l_data) -1)):
            count2 = count1 + 1
            while (count2 < len(l_data)):
                if (len(l_data[count1]) > len(l_data[count2])):
                    temp = l_data[count1]
                    l_data[count1] = l_data[count2]
                    l_data[count2] = temp
                count2 = count2 + 1
            count1 = count1 + 1

    return(l_data)

#========================= Write the NG label in the header file =======================
#=======================================================================================
def NGlabelheaderfilecreation(dir_path, file_name, data, data_type, data_size, is_asil):
    "This function is used to create the NG label in the header file"

    #Define local variable(s) here
    l_dir_path = dir_path
    l_file_name = dir_path + "/" + file_name
    l_header_list = common_infor.header_file_list
    l_prefix_pragma = common_infor.prefix_pragma
    l_list_pragma = common_infor.list_pragma
    l_data = sortarray(data, "No")
    l_data = removeduplicate(l_data)
    l_data_type = data_type
    l_data_size = data_size
    l_temp = file_name.split(".")[0]
    l_header_file = l_temp.upper() + "_H_"
    l_mode_write = "a+"

    #Some common symbols using in program
    l_start = "_START"
    l_end = "_END"
    l_include = "#include "
    l_ifndef = "#ifndef "
    l_endif = "#endif"
    l_define = "#define "
    l_extern = "extern "
    l_notify = "(None_Type)"

    #Procedure to create the NG label in header file
    #Step 1: Create the output folder if it is not existed and reset historied data
    common.makedir(l_dir_path)
    deletetextfile(l_file_name)

    #Step 2: Open the NG label in header file
    l_ojb_file = open(l_file_name, l_mode_write)

    #Step 3: Create the header of header file.
    l_ojb_file.write("/* " + file_name + " */ \n \n")
    l_ojb_file.write(l_ifndef + l_header_file + "\n")
    l_ojb_file.write(l_define + l_header_file + "\n \n")

    if(is_asil != "Yes"):
        l_ojb_file.write(l_include + "\"" + l_header_list[2] + "\"")
    else:
        l_ojb_file.write(l_include + "\"" + l_header_list[2] + "\"" + "\n")
        l_ojb_file.write(l_include + "\"" + l_header_list[0] + "\""+ "\n")

    #Step 4: Create the main content of header file.
    l_ojb_file.write("\n")
    if(l_data != ['NULL']):
        for each_label in l_data:
            l_data_size_temp = int(l_data_size.setdefault(each_label, 124))
            l_ojb_file.write("\n")
            l_ojb_file.write(l_ifndef + each_label + "\n")
            if (l_data_size_temp == 1):
                l_ojb_file.write(l_extern + \
                                 l_data_type.setdefault(each_label, l_notify) + \
                                 " " + \
                                 each_label + \
                                 ";\n")
            else:
                l_ojb_file.write(l_extern + \
                                 l_data_type.setdefault(each_label, l_notify) + \
                                 " " + \
                                 each_label + 
                                 "[" + \
                                 str(l_data_size_temp) + \
                                 "];" +\
                                 "\n")
            l_ojb_file.write(l_endif + "\n")

    #Step 5: Create the end of header file.
    l_ojb_file.write("\n" + l_endif + " /* " + l_header_file + " */" + "\n")
    l_ojb_file.close()

    return()

#===================== Write the NG label in The source file ===========================
#=======================================================================================
def NGlabelsourcefilecreation(dir_path, file_name, data, data_type, data_size, is_asil):
    "This function is used to create the NG label in the source file"

    #Define local variable(s) here
    l_dir_path = dir_path
    l_file_name = dir_path + "/" + file_name
    l_header_list = common_infor.header_file_list
    l_prefix_pragma = common_infor.prefix_pragma
    l_list_pragma = common_infor.list_pragma
    l_temp = file_name.split(".")[0]
    l_header_file = l_temp + ".h"
    l_data = sortarray(data, "No")
    l_data = removeduplicate(l_data)
    l_data_type = data_type
    l_data_size = data_size
    l_mode_write = "a+"

    #Some common symbols using in program
    l_start = "_START"
    l_end = "_END"
    l_include = "#include "
    l_ifndef = "#ifndef "
    l_define = "#define "
    l_endif = "#endif"
    l_tab = "   "
    l_notify = "(None_Type)"
    l_app = "_APP"
    l_pra = "#pragma section"

    #Procedure to create the NG label in source file
    #Step 1: Create the output folder if it is not existed and reset historied data
    common.makedir(l_dir_path)
    deletetextfile(l_file_name)

    #Step 2: Open the NG label source file
    l_ojb_file = open(l_file_name, l_mode_write)

    #Step 3: Create the header of the source file.
    l_ojb_file.write("/* " + file_name + " */ \n \n")
    if(is_asil != "Yes"):
        l_ojb_file.write(l_include + "\"" + l_header_list[5] + "\"" + "\n")
        l_ojb_file.write(l_include + "\"" + l_header_file + "\"" + "\n \n")
        l_ojb_file.write(l_pra + " " + l_app + "\n \n")
    else:
        l_ojb_file.write(l_include + "\"" + l_header_list[3] + "\"" + "\n")
        l_ojb_file.write(l_include + "\"" + l_header_file + "\"" + "\n \n")
        l_ojb_file.write(l_define + l_prefix_pragma[1] + l_list_pragma[0] + l_start + "\n")
        l_ojb_file.write(l_include + "\"" + l_header_list[1] + "\"" + "\n \n")

    #Step 4: Create the main content of the source file.
    if(l_data != ['NULL']):
        for each_label in l_data:
            l_data_size_temp = int(l_data_size.setdefault(each_label, 124))
            l_ojb_file.write(l_ifndef + each_label + "\n")
            if(l_data_size_temp == 1):
                l_ojb_file.write(l_data_type.setdefault(each_label, l_notify) + \
                                 l_tab + \
                                 each_label + \
                                 ";" + \
                                 "\n")
            else:
                l_ojb_file.write(l_data_type.setdefault(each_label, l_notify) + \
                                 l_tab + each_label + \
                                 "[" + str(l_data_size_temp) + \
                                 "];" + \
                                 "\n")
            l_ojb_file.write(l_endif + "\n\n")

    #Step 5: Create the end of the source file.
    if(is_asil != "Yes"):
        l_ojb_file.write(l_pra + "\n")
    else:
        l_ojb_file.write(l_define + l_prefix_pragma[1] + l_list_pragma[0] + l_end + "\n")
        l_ojb_file.write(l_include + "\"" + l_header_list[1] + "\"" + "\n")

    l_ojb_file.close()

    return()

#================== Write the NG callback function in the source file ==================
#=======================================================================================
def NGcallbacksourcefilecreation(dir_out_path, file_name, data, is_asil):
    "This function is used to create the NG callback function in the source file"

    #Define local variable(s) here
    l_dir_out_path = dir_out_path
    l_file_name = l_dir_out_path + "/" + file_name
    l_data = sortarray(data, "No")
    l_data = removeduplicate(l_data)
    l_header_list = common_infor.header_file_list
    l_notify = common_infor.callback_notification
    l_prefix_pragma = common_infor.prefix_pragma
    l_list_pragma = common_infor.list_pragma
    l_temp = file_name.split(".")[0]
    l_header_file = l_temp + ".h"
    l_mode_write = "a+"

    #Some common symbols using in program
    l_start = "_START"
    l_end = "_END"
    l_include = "#include "
    l_ifndef = "#ifndef "
    l_endif = "#endif"
    l_define = "#define "
    l_void = "void"
    l_tab = "   "
    l_type_of_data = "uchar8 "

    #Procedure to create the NG callback function in source file
    #Step 1: Create the output folder if it is not existed and reset historied data
    common.makedir(l_dir_out_path)
    deletetextfile(l_file_name)

    #Step 2: Open the NG callback function source file
    l_ojb_file = open(l_file_name, l_mode_write)

    #Step 3: Create the header of the source file.
    l_ojb_file.write("/* " + file_name + " */ \n")
    if(is_asil != "Yes"):
        l_ojb_file.write("/* " + l_notify[0] + " */ \n \n")
        l_ojb_file.write(l_include + "\"" + l_header_list[7] + "\"" + "\n")
        l_ojb_file.write(l_include + "\"" + l_header_file + "\"" + "\n")
    else:
        l_ojb_file.write(l_include + "\"" + l_header_file + "\"" + "\n \n")
        l_ojb_file.write(l_define + l_prefix_pragma[1] + l_list_pragma[1] + l_start + "\n")
        l_ojb_file.write(l_include + "\"" + l_header_list[1] + "\"" + "\n")

    #Step 4: Create main content of source file
    #Define the variables for the callback function here
    l_variable_list_cb = variableconvertcb(l_data, is_asil)
    for each_val in l_variable_list_cb:
       l_ojb_file.write("\n")
       l_ojb_file.write(l_ifndef + each_val + "\n")
       l_ojb_file.write(l_tab + l_type_of_data + each_val + ";" + "\n")
       l_ojb_file.write(l_endif + "\n")

    l_ojb_file.write("\n")
    if(is_asil == "Yes"):
        l_ojb_file.write("\n")
        l_ojb_file.write(l_define + l_prefix_pragma[1] + l_list_pragma[1] + l_end + "\n")
        l_ojb_file.write(l_include + "\"" + l_header_list[1] + "\"" + "\n \n")
        l_ojb_file.write(l_define + l_prefix_pragma[1] + l_list_pragma[2] + l_start + "\n")
        l_ojb_file.write(l_include + "\"" + l_header_list[1] + "\"" + "\n\n")

    #Define the callback function
    if(l_data != ['NULL']):
        for each_callback in range(len(l_data)):
            l_ojb_file.write("\n" + l_ifndef + l_data[each_callback] + "\n")
            l_ojb_file.write(l_void + " " + l_data[each_callback] + "(" + l_void + ")" + "\n")
            l_ojb_file.write("{ \n")
            l_ojb_file.write(l_tab + l_variable_list_cb[each_callback] + "++;\n")
            l_ojb_file.write("}\n")
            l_ojb_file.write(l_endif + "\n")

    #Step 5: Create the end of the source file.
    if(is_asil == "Yes"):
        l_ojb_file.write("\n")
        l_ojb_file.write(l_define + l_prefix_pragma[1] + l_list_pragma[2] + l_end + "\n")
        l_ojb_file.write(l_include + "\"" + l_header_list[1] + "\"" + "\n")
    l_ojb_file.close()

    return()

#================= Write the NG callback function in the header file ===================
#=======================================================================================
def NGcallbackheaderfilecreation(dir_out_path, file_name, data, is_asil):
    "This function is used to create the NG callback function in the header file"

    #Define local variable(s) here
    l_dir_out_path = dir_out_path
    l_file_name = l_dir_out_path + "/" + file_name
    l_data = sortarray(data, "No")
    l_data = removeduplicate(l_data)
    l_header_list = common_infor.header_file_list
    l_is_asil = is_asil
    l_prefix_pragma = common_infor.prefix_pragma
    l_list_pragma = common_infor.list_pragma
    l_start = "_START"
    l_end = "_END"
    l_temp = file_name.split(".")[0]
    l_header_file = l_temp.upper() + "_H_"
    l_mode_write = "a+"

    #Some common symbols using in program
    l_void = "void"
    l_include = "#include "
    l_ifndef = "#ifndef "
    l_define = "#define "
    l_endif = "#endif"
    l_extern = "extern "

    #Procedure to create the NG callback function header file
    #Step 1: Create the output folder if it is not existed and reset historied data
    common.makedir(l_dir_out_path)
    deletetextfile(l_file_name)

    #Step 2: Open the NG callback function output header file
    l_ojb_file = open(l_file_name, l_mode_write)

    #Step 3: Create the header of the header file.
    l_ojb_file.write("/* " + file_name + " */ \n \n")
    l_ojb_file.write(l_ifndef + l_header_file + "\n")
    l_ojb_file.write(l_define + l_header_file + "\n \n")

    if(l_is_asil != "Yes"):
        l_ojb_file.write(l_include + "\"" + l_header_list[4] + "\"" + "\n")
    else:
        l_ojb_file.write(l_include + "\"" + l_header_list[3] + "\"" + "\n")
        l_ojb_file.write(l_include + "\"" + l_header_list[2] + "\"" + "\n")
        #l_ojb_file.write(l_include + "\"" + l_header_list[6] + "\"" + "\n")

    #Step 4: Create the main content of the header file.
    if(l_data != ['NULL']):
        for each_callback in l_data:
            l_ojb_file.write("\n")
            l_ojb_file.write(l_ifndef + each_callback + "\n")
            l_ojb_file.write(l_extern + l_void + " " + each_callback + "(" + l_void + ");" + "\n")
            l_ojb_file.write(l_endif + "\n")

    #Step 5: Create the end of the header file.
    l_ojb_file.write("\n" + l_endif + " /* " + l_header_file + " */" + "\n")
    l_ojb_file.close()

    return()

#============== Exchange the ending format of line from Unix to Window =================
#=======================================================================================
def convert_ending_line_format(is_linux_to_window):
    """This function is used to convert the ending format
    of each line from linux to window and vice versa"""

    #Define local variables here
    cv_input_folder_list = [common_infor.NG_output_folder_lb]
    cv_input_folder_list.append(common_infor.NG_output_folder_cb)
    cv_extension_file = ["c", "h"]
    WINDOWS_LINE_ENDING = b'\r\n'
    UNIX_LINE_ENDING = b'\n'

    for each_folder in cv_input_folder_list:
        for each_extension_file in cv_extension_file:
            cv_list_files_temp = common.getfilelist(each_folder, \
                                                    each_extension_file)
            for each_file in cv_list_files_temp:
                cv_obj_file = open(each_folder + "/" + each_file, "rb+")
                cv_data = cv_obj_file.read()
                cv_obj_file.close()
                if (is_linux_to_window == "Yes"):
                    cv_data = cv_data.replace(UNIX_LINE_ENDING, WINDOWS_LINE_ENDING)
                else:
                    cv_data = cv_data.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
                
                cv_obj_file = open(each_folder + "/" + each_file, "wb")
                cv_obj_file.write(cv_data)
                cv_obj_file.close()

    return()