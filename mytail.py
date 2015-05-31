#!/usr/bin/env python


import sys



def watch(filename, seek):
        fs = open(filename,'r')
        fs.seek(0,2)

        while True:
                line = fs.readline().strip()
                if len(line) > 0:
                        line = line.replace(seek, seek.upper())
                        yield(line)
        #       if seek in line:
        #               yield(line)

filename = sys.argv[1]
seek = sys.argv[2]

for line in watch(filename, seek):
        print line
