#!/usr/bin/env python3

import sys

inputfile = None
outputfile = None

def main():
    if len(sys.argv) <= 1:
        print("usage: programm file returntype")
        return
    
    global inputfile
    inputfile = open(sys.argv[1])
    if inputfile == None:
        print('file: %s not found', sys.argv[1])
        return

    global outputfile
    outputfile = open("resfunc.py", 'w')

    outputfile.write('def getValue(x):\n')

    for line in inputfile:
        if line == '\n':
            continue
        handleline(line)

    inputfile.close()

    outputfile.write('\0')
    outputfile.close()

def handleline(line):
    parts = line.split(':')

    global outputfile
    outputfile.write("    if ")

    print(parts)

    placeand = False

    for part in parts:
        spart = part.split(' ')
        spart = [x for x in spart if x]
        print(spart)

        if spart[0] == 'out':
            outputfile.write(':\n        return ' + ' '.join(spart[1:]))
            continue

        if spart[0] == '&&':
            outputfile.write(' and ')
            continue

        if spart[0] == '||':
            outputfile.write(' or ')
            continue

        if spart[0] == '[':
            if spart[1] == '#':
                placeand = False
                continue
            placeand = True
            outputfile.write(' x >= '+ spart[1])
            continue
        if spart[0] == ']':
            if spart[1] == '#':
                placeand = False
                continue
            placeand = True
            outputfile.write(' x > '+ spart[1])
            continue

        if spart[1] == '[':
            if spart[0] == '#':
                continue
            if placeand:
                outputfile.write(' and')
            outputfile.write(' x < ' + spart[0])
            continue
        if spart[1] == ']':
            if spart[0] == '#':
                continue
            if placeand:
                outputfile.write(' and')
            outputfile.write(' x <= ' + spart[0])
            continue


if __name__ == "__main__":
    main()
