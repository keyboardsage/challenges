#!/usr/bin/python

import sys
import datetime
import time

staticDate = datetime.date.today()
for line in open (sys.argv[1], "r"):
    tempList = line.rstrip().split(' ')
    timeTempList1 = map(int, tempList[0].split(':'))
    timeTempList2 = map(int, tempList[1].split(':'))
    time1 = datetime.time(timeTempList1[0], timeTempList1[1], timeTempList2[2])
    time2 = datetime.time(timeTempList2[0], timeTempList2[1], timeTempList2[2])
    FMT = '%H:%M:%S'
    theOutput = None
    if time1 > time2:
        theOutput = datetime.datetime.strptime(tempList[0],FMT) - datetime.datetime.strptime(tempList[1],FMT)
    else:
        theOutput = datetime.datetime.strptime(tempList[1],FMT) - datetime.datetime.strptime(tempList[0],FMT)
    theOutput = theOutput if len(str(theOutput)) != 7 else "0" + str(theOutput)
    print theOutput
