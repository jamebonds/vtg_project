import time
import RPi.GPIO as GPIO

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

        print('pulse:{0} 2:{1} 3:{2} 4:{3} 5:{4} 6:{5} 7:{6} 8:{7} 9:{8} 10:{9} 11:{10}'.format(input_value,in2,in3,in4,in5,in6,in7,in8,in9,in10,in11))