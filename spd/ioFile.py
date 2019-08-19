import pandas as pd
import time
import RPi.GPIO as GPIO
import os

# name CSV FILE
filename = 'SPD-xx'

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
in4buffer = 0
in8buffer = 1
mm = 0
yard = 0
c = 285.00
p = 600.00

# 1 - 3
#os.system('sudo mount.cifs //172.16.54.17/iotData /media/AIP -o rw,uid=pi,password=eseuser')
# 4 - 6
#os.system('sudo mount.cifs //172.16.54.14/iotData /media/AIP -o rw,uid=pi,password=eseuser')
while True :
        input_value = GPIO.input(18)
        in2 = GPIO.input(23)
        in3 = GPIO.input(24)
        in4 = GPIO.input(25)
        in5 = GPIO.input(5)
        in6 = GPIO.input(6)
        in7 = GPIO.input(13)
        in8 = GPIO.input(19)
        in9 = GPIO.input(26)
        in10 = GPIO.input(8)
        in11 = GPIO.input(7)
        if (in11 ==11):
            if(in2 == 1 and in3 == 1 and in4 == 1 and in5 == 1 and in6 == 0 and in7 ==1 and in8 == 1 and in9 == 1): # Spreading with material
                if(input_value != buffer and input_value == 1):
                        counter +=1
                        mm = (c/p)*counter
                        print("plus ",counter , " mm " , mm)
                buffer = input_value
            elif(in2 == 1 and in3 == 1 and in5 == 1  and in6 == 1 and in7 == 1 and in8 == 0 and in8buffer == 1 and in9 == 1): # Cut Spreading4
                os.system('sudo mount.cifs //172.16.54.17/iotData /media/AIP -o rw,uid=pi,password=eseuser')
                sumLenght = sumLenght+mm
                yard = sumLenght*0.00109361
                counter = 0
                #mm = 0
                print("Cut : sumLenght (mm)",sumLenght," sumLenght (yard)",yard)
                print('IO Read : Meter : {0:.2f} M , Yard {1:.2f} y'.format(sumLenght/1000,yard))
                datafram = pd.DataFrame({'YD': ['{0:.2f}'.format(yard)], 'MT': ['{0:.2f}'.format(sumLenght/1000)]})
                #datafram2 = pd.DataFrame({'YD':['{0:.2f}'.format(yard)], 'MT': ['{0:.2f}'.format(sumLenght/1000)]} , 'Index'[i+1])
                try:
                    #os.system('sudo mount.cifs //172.16.54.17/iotData /media/AIP -o rw,uid=pi,password=eseuser')
                    time.sleep(0.5)
                    datafram.to_csv('/media/AIP/{0}.csv'.format(filename),encoding="iso-8859-1",index=False)
                    #datafram2.to_csv('/home/pi/ioRead/')
                except IOError :
                    print("Error")
                    pass
                os.system('sudo umount /media/AIP')
                #yard = 0
                #sumLenght = 0
                time.sleep(2)
            elif(in2 == 1 and in3 == 1 and in4 == 0 and in4buffer == 1 and in5 == 1 and in6 == 0 and in7 == 1 and in8 == 1 and in9 == 1):   # No material
                sumLenght = sumLenght+mm
                yard = sumLenght*0.00109361
                mm = 0
                print("No Material ","sumLenght (mm)",sumLenght," sumLenght (yard)",yard)
                counter = 0
                time.sleep(1)
            # elif (in10 == 0 and closeJobBuffer == 1):  # CloseJob
            #     # sumLenght = sumLenght+mm
            #     yard = sumLenght * 0.00109361
            #     print("Close Job ", "sumLenght (mm)", sumLenght, " sumLenght (yard)", yard)
            #     mm = 0
            #     counter = 0
            #     sumLenght = 0
            closeJobBuffer = in10
            in4buffer = in4
            in8buffer = in8
        elif(in11 == 0 ) :
            mm= 0
            sumLenght = 0
