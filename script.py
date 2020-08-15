
"""
@author: SCHERIC
"""


# !/usr/bin/python

import sys
import re
import time

time_start = time.time()

sourceFile = sys.argv[1]

add_count = 0

debug = 1

if debug >= 1:
    print(sourceFile)

# M73 P86 R6
#      %%  t

with open(sourceFile, "r+") as file:
    lines = file.readlines()

    for line_number in range(len(lines)):
        new_line = lines[line_number]

        if len(new_line) > 0:
            # Write original line to buffer
            file.write(new_line)

            # find specific line
            stringMatch = re.search('^M73 P(.*) R(.*)', new_line)
            if stringMatch:
                # do something when hit

                # Parse gcode line
                string = stringMatch.string
                parsed = string.split(' ')

                parsed[1] = parsed[1][1:]
                parsed[2] = parsed[2][1:]

                output = 'm117 ' + parsed[1] + '% ' + parsed[2] + " minutes left"

                if debug >= 2:
                    print(str(stringMatch) + str(output))

                # save new line to file
                file.write(f"{output}\n")

                add_count = add_count + 1

# return file to proses
file.close()

time_end = time.time()

if debug >= 1:
    print(f"added {add_count} extra m117 lines from {sourceFile}")
    print(f"elapsed time: {round(time_end - time_start,4)} S")

if debug >= 1:
    sec = input('wait for user input.\n')
