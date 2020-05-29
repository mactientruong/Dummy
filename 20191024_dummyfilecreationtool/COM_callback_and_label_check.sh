#!/usr/bin/bash
#File name: COM_callback_and_label_check.sh

#===================================== Revision history ================================
#=======================================================================================
#
#   UPDATE HISTORY     DATE        AUTHOR          MODIFIED POINT
#       Creation    2019.05.15  Mac Tien Truong     Create new

function main
{
    cd Tools
    echo ""
    echo ""
    echo "********************** Execute the input_file_creation tool ********************"
    echo "********************************************************************************"
    python3 input_file_creation.py
    echo ""
    echo ""
    echo "****************************** Execute the core_tool ***************************"
    echo "********************************************************************************"
    python3 core_tool.py
    echo ""
    echo ""
    echo "********************* Execute the dummy_file_creation tool *********************"
    echo "********************************************************************************"
    python3 dummy_file_creation.py
    echo "********************************************************************************"
    echo "********************************** Finished ************************************"

    exit 1
}

main