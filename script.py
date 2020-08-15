# -*- coding: utf-8 -*-
"""

@author: SCHERIC
"""


#!/usr/bin/python

import sys
import re
import os
import time

time_start = time.time()

sourceFile=sys.argv[1]

add_count=0

debug = 1

# Read the ENTIRE g-code file into memory
with open(sourceFile, "r") as f:
    lines = f.readlines()

destFile = re.sub('\.gcode$','',sourceFile)
os.rename(sourceFile,sourceFile)
destFile = re.sub('\.gcode$','',sourceFile)
destFile = destFile + '.gcode'

if debug >=1:
    print(sourceFile)
    print(destFile)
    
#M73 P86 R6
#     %%  t

with open(destFile, "w") as of:
    for lIndex in range(len(lines)):
        oline = lines[lIndex]
        # Parse gcode line
        parts = oline.split(';', 1)
        if len(parts) > 0:
            # Parse command
            command = parts[0].strip()

            if command:
                stringMatch = re.search ('^M73 P(.*) R(.*)', command)
                if stringMatch:
                    # Insert code to do something
                    
                    string=stringMatch.string
                    
                    var = string.split(' ')
                    
                    var[1] = var[1][1:]
                    var[2] = var[2][1:]
                    
                    output = 'm117 ' + var[1] + '% ' + var[2] + " minutes"
                    
                    if debug >=2:
                        print(str(stringMatch) + str(output))
            
                    of.write(f"{output}\n")

                    add_count = add_count+1
                    
            
            # Write original line       
            of.write(oline)
of.close()
f.close()

time_end = time.time()

if debug >=1:
    print(f"added {add_count} extra m117 lines from {destFile}")
    print(f"elapsed time: {round(time_end - time_start,4)} S")

if debug >=1:
    sec = input('wait for user input.\n')

