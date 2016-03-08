#!/usr/bin/env python3
__author__ = 'darwin'


debugMode = False

print("Debug Mode is off by default, if you want to Debug please press 'y' ")
x = input()

if x == 'y':
    debugMode = True


def extractData(inputFile,outputFile):


    txt = open(inputFile)
    json = open(outputFile, 'w')
    rawData = txt.readlines()


    count = 1
    lastPosition = len(rawData)

    firstpostion = True


    for x in rawData:

        if firstpostion:
            json.write("{")
            json.write("\n")
            firstpostion = False

        x = x.strip('\n')

        if count != lastPosition:
            if len(x)!= 1:
                json.writelines("\t" + "\"" + str(count) + "\":" + "\"" + str(x) + "\"" + "," + "\n")
        elif count == lastPosition:
            json.writelines("\t" + "\"" + str(count) + "\":" + "\"" + str(x) + "\"" + "\n"+"}")

        count += 1


    if debugMode:
        print()
        print("This is Report is shown for DEBUG purpose")
        print()
        print(rawData)
        print()
        print("The total datas found in this file is")
        print(str(len(rawData)))
        print()
        print("End of DEBUG Report")


extractData("RawData", "Json")

input()
