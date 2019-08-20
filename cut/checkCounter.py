import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

bit1 ='x'
bit2 ='x'
bit3 ='x'
bit10 ='x'

GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(7, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(16, GPIO.IN)

while 1 :
    bit4 = GPIO.input(14)
    bit5 = GPIO.input(15)
    bit6 = GPIO.input(18)
    bit7 = GPIO.input(23)
    bit8 = GPIO.input(24)
    bit9 = GPIO.input(25)
    bit11 = GPIO.input(8)
    bit12 = GPIO.input(7)
    bit13 = GPIO.input(12)
    bit14 = GPIO.input(16)
    print('B:{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}'.format(bit14,bit13,bit12,bit11,bit10,bit9,bit8,bit7,bit6,bit5,bit4,bit3,bit2,bit1))