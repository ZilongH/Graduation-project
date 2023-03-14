import os
import time
import datetime

# begin = time.time()
# os.system('rsync -a --delete rsync://repository.lacnic.net/rpki ./RPKI_code/rpki_lacnic')
# replace_lacnic = time.time()
# os.system('rsync -a --delete rsync://repository.lacnic.net/rpki ./RPKI_code/rpki_lacnic_'+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+'')
# empty_lacnic = time.time()
# replace_apnic = time.time()
# os.system('rsync -a --delete rsync://rpki.apnic.net/repository/ ./RPKI_code/rpki_apnic_'+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+'')
# os.system('rsync -a --delete rsync://rpki.apnic.net/member_repository ./RPKI_code/rpki_apnic_member_repository_'+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+'')
# empty_apnic = time.time()
# print(replace_lacnic-begin, empty_lacnic-replace_lacnic, empty_apnic-replace_apnic)
# f = open('./RPKI_ftp/routinator_2022-05-22_afrinic.txt', 'r')
# f.read()
# f.close()
print(datetime.date.today())