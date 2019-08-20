import csv
import NPi.GPIO as GPIO
import time
import os ,sys
from datetime import datetime
# pin GPIO
pinSW = 8

# PATH File
fileAip = '/media/AIP/Cut-01.csv'
fileCut = '/media/CuttingMachine/'

# Config Mount I/O to Windows
cutDrive = 'sudo mount.cifs //PathCutting/data /media/AIP -o rw,uid=pi,password=eseuser'
aipDrive = 'sudo mount.cifs //PathAIP/data /nedia/AIP -o rw,uid=pi,password=eseuser'

# Config CSV
mt = 'MT'
yd = 'YD'
header =  [yd,mt]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinSW,GPIO.IN)

reader = csv.reader(open("csvfile.csv"), delimiter=";")
included_cols = [22]
count = 0
content = []

def openFile():
    # os.system(cutDrive)
    now = datetime.now()  # current date and time
    nowdate = now.strftime("%Y%m%d")
    fileReport = 'Reporting_' + nowdate + '-Job.csv'
    while (os.path.ismount('/media/AIP') == False):
        os.system(cutDrive)
    try:
        reader = csv.reader(open(fileCut+fileReport), delimiter=";")
        for row in reader:
            content.append(row[22])
        num_list = len(content)
        num_list_target = num_list - 1
        dataValue = content[num_list_target - 1]
        # print(content[num_list_target - 1])
    except IOError :
        print('ERROR :'+IOError)
    return dataValue

def writeFile(value):
    # os.system(aipDrive)
    # f = open(fileAip, "a")
    # f.write(value)
    while (os.path.ismount('/media/AIP') == False):
        os.system(cutDrive)
    try:
        with open(fileAip,'w',newline='') as csvfile :
            writer = csv.DictWriter(csvfile,fieldnames=header)
            writer.writeheader()
            writer.writerow({yd:(value*1.0936133),mt:value})
    except IOError:
        print('ERROR' +IOError)
    # f.close()


## ------ MAIN ---------
while True:
    # inputSW = 0
    inputSW = GPIO.input(pinSW)
    if(inputSW == 1):
        time.sleep(1)
        valueCSV = openFile()
        writeFile(valueCSV)

