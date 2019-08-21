import os ,sys

print('setup program')

try:
    os.system('sudo apt-get update -y')
    os.system('sudo apt-get install cifs-utils -y')
    os.system('sudo apt-get install python-pandas -y && sudo apt-get install python3-pandas -y')
    os.system('sudo chmod 775 cut/* && sudo chmod 775 spd/*')
except IOError :
    print('Error :' + IOError)
finally:
    print('Exit Program ..')