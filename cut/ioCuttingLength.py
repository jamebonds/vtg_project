import csv
#import NPi.GPIO as GPIO
import time
import os ,sys

fileName  ='CUT'
pinSW = 6
cutDrive = 'sudo mount.cifs //PathCutting/data /media/AIP -o rw,uid=pi,password=eseuser'
aipDrive = 'sudo mount.cifs //PathAIP/data /nedia/AIP -o rw,uid=pi,password=eseuser'
fileReport = 'Reporting_'  +'-Job.xls'
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(pinSW,GPIO.IN)

reader = csv.reader(open("csvfile.csv"), delimiter=";")
included_cols = [22]
count = 0
content = []

def openFile():
    os.system(cutDrive)
    while (os.path.ismount('/media/AIP') == False):
        os.system(cutDrive)
    try:
        reader = csv.reader(open("csvfile.csv"), delimiter=";")
        for row in reader:
            content.append(row[22])
        num_list = len(content)
        num_list_target = num_list - 1
        dataValue = content[num_list_target - 1]
        print(content[num_list_target - 1])
    except IOError :
        print('ERROR :'+IOError)
    return dataValue

def writeFile():
    os.system(aipDrive)
    while (os.path.ismount('/media/AIP') == False):
        os.system(cutDrive)
    try:
        print('hello')
    except IOError:
        print('hello')




while True:
    inputSW = 0
    #inputSW = GPIO.input(pinSW)
    if(inputSW == 1):
        print('hello World')
        time.sleep(1)
        valueCSV = openFile()

