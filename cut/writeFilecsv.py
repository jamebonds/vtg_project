import os
import csv
# value = 20.31
# mt = 'MT'
# yd =  'YD'
if(os.path.ismount('/media/AIP') == True):
    print('!!!!')
else :
    print('????')

# with  open('csvtest.csv','w',newline='') as csvfile:
#     header =  ['YD','MT']
#     writer = csv.DictWriter(csvfile,fieldnames=header)
#     writer.writeheader()
#     writer.writerow({yd:value,mt:value})
    # writer.writerow({mt: 'Baked', yd: 'Beans'})
# writer.writerow({'MT':'WTF','YD':'WTF'})

