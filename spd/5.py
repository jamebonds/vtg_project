import pandas as pd
import time
import RPi.GPIO as GPIO
import os
import array

# name CSV FILE
filename = 'SPD-05'
fileLog = 'SPD-LOG-xx'

compensationMM = 43.81
compensationYard = 0.0479111986

# 1 - 3
#os.system('sudo mount.cifs //172.16.54.17/iotData /media/AIP -o rw,uid=pi,password=eseuser')
# 4 - 6
#os.system('sudo mount.cifs //172.16.54.14/iotData /media/AIP -o rw,uid=pi,password=eseuser')
ioConnectMount = 'sudo mount.cifs //172.16.54.14/iotData /media/AIP -o rw,uid=pi,password=eseuser'
pathLog = '/home/pi/VTG/SPD-LOG.csv'
osUnMount = 'sudo umount /media/AIP'

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(8,GPIO.IN)
GPIO.setup(7,GPIO.IN)

buffer = 0      # Buffer of pluse value
counter = 0     # pluse counter
closeJobBuffer = 0      # Last stage of close job
sumLenght = 0
sumLog = 0
in4buffer = 0
in8buffer = 1
mm = 0
yard = 0
c = 285.00
p = 600.00
df =pd.DataFrame({'mm':[]})
i = 0

def writeFile (datafram):
    while (os.path.ismount('/media/AIP') == False):
        os.system(ioConnectMount)
    try:
        print('WriteFile CSV')
        datafram.to_csv('/media/AIP/{0}.csv'.format(filename), encoding="iso-8859-1", index=False)
        #f.write('\n{0:.4f},{1:.4f},{2}'.format(sumLog, yardLog, time.time()))
        time.sleep(0.3)
    except IOError:
        print("Error")
        pass
        #f.close()

while True :
        input_value = GPIO.input(18)
        in2 = GPIO.input(23)
        in3 = GPIO.input(24)
        in4 = GPIO.input(25)
        in5 = GPIO.input(5)
        in6 = GPIO.input(6)
        in7 = GPIO.input(13)
        in8 = GPIO.input(19) # GPIO.input(22) Cut Spreading 2
        in9 = GPIO.input(26)
        in10 = GPIO.input(8)
        in11 = GPIO.input(7)
        if (in11 ==0):
            if(in2 == 1 and in3 == 1 and in4 == 1 and in5 == 1 and in6 == 0 and in7 ==1 and in8 == 1 and in9 == 1): # Spreading with material
                if(input_value != buffer and input_value == 1):
                        counter +=1
                        mm = (c/p)*counter
                        #print("pulse ",counter , " mm " , mm)
                buffer = input_value
            elif(in2 == 1 and in3 == 1 and in5 == 1  and in6 == 1 and in7 == 1 and in8 == 0 and in8buffer == 1 and in9 == 1): # Cut Spreadin 2-6
            #elif (in2 == 0 and in3 == 1 and in5 == 1 and in6 == 1 and in7 == 1 and in8 == 0 and in8buffer == 1 and in9 == 1):  # Cut Spreading 1
                os.system(ioConnectMount)
                #f = open(pathLog,'a')
                time.sleep(0.3)
                sumLenght = sumLenght+mm + compensationMM
                #sumLog = mm
                yard = sumLenght*0.00109361 + compensationYard
                #yardLog  = mm *0.00109361
                counter = 0
                #print("I/O Cuting  : sumLenght (mm)",sumLog," sumLenght (yard)",yardLog)
                datafram = pd.DataFrame({'YD': ['{0:.4f}'.format(yard)], 'MT': ['{0:.4f}'.format(sumLenght/1000)]})
                writeFile(datafram)
                os.system(osUnMount)
                #sumLog = 0
                #yardLog = 0
                mm= 0
                #f.close()
                time.sleep(2)
            elif(in2 == 1 and in3 == 1 and in4 == 0 and in4buffer == 1 and in5 == 1 and in6 == 0 and in7 == 1 and in8 == 1 and in9 == 1):   # No material
                os.system(ioConnectMount)
                #f = open(pathLog, 'a')
                time.sleep(0.3)
                sumLenght = sumLenght+mm + compensationMM
                yard = sumLenght*0.00109361 + compensationYard
                #sumLog = mm
                #yardLog = mm *0.00109361 + compensationYard
                mm = 0
                print("No Material ","sumLenght (mm)",sumLenght," sumLenght (yard)",yard)
                datafram = pd.DataFrame({'YD': ['{0:.4f}'.format(yard)], 'MT': ['{0:.4f}'.format(sumLenght / 1000)]})
                writeFile(datafram)
                counter = 0
                #sumLog = 0
                #ardLog = 0
                #f.close()
                time.sleep(1)
            closeJobBuffer = in10
            in4buffer = in4
            in8buffer = in8
        elif (in11 ==1 and in2 == 0 and in5 == 1 and in6 == 1) :
            mm= 0
            sumLenght = 0





