#!/usr/bin/python
from sas7bdat import SAS7BDAT
import sys

#################################################################################
# CONVERT A SAS FILE TO CSV
# - PATH TO INPUT FILE
# - PATH TO OUTPUT FILE
#################################################################################
def main():
    if len(sys.argv) < 2:
        print( "ERROR: MISSING ARGUMENTS" )
        print_usage( sys.argv )
        exit(1)
    else:
        input = sys.argv[1]
        output = sys.argv[2]

        convert_sas_file( input, output )

#################################################################################
def print_usage(args):
    print("USAGE ")
    print(args[0], "<INPUT SAS7 FILE> <OUTPUT CSV FILE NAME AND PATH>")


#################################################################################
# CONVERT A SAS FILE TO CSV
#################################################################################
def convert_sas_file( input, output ):
    with SAS7BDAT( input ) as reader:
        df = reader.to_data_frame()
    df.to_csv( output, index=False )


#################################################################################
if __name__ == "__main__": main()

