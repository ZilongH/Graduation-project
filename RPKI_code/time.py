import os
import time
import datetime

# rsync -r rsync://rpki.afrinic.net/repository ./RPKI_code/rpki_afrinic
# rsync -r rsymc://rpki.arin.net/repository ./RPKI_code/rpki_arin
# rsync -r rsync://rpki.ripe.net/repository ./RPKI_code/rpki_ripe
# rsync -r rsync://repository.lacnic.net/rpki ./RPKI_code/rpki_lacnic
# rsync -r rsync://rpki.apnic.net/repository ./RPKI_code/rpki_apnic

begin = time.time()
os.system('rsync -a --delete rsync://rpki.afrinic.net/repository/ ./RPKI_code/rpki_afrinic')
replace_afrinic = time.time()
os.system('rsync -a --delete rsync://rpki.afrinic.net/repository/ ./RPKI_code/rpki_afrinic_'+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+'')
empty_afrinic = time.time()
os.system('rsync -a --delete rsync://rpki.arin.net/repository/ ./RPKI_code/rpki_arin')
replace_arin = time.time()
os.system('rsync -a --delete rsync://rpki.arin.net/repository/ ./RPKI_code/rpki_arin_'+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+'')
empty_arin = time.time()
os.system('rsync -a --delete rsync://rpki.apnic.net/repository/ ./RPKI_code/rpki_apnic')
os.system('rsync -a --delete rsync://rpki.apnic.net/member_repository ./RPKI_code/rpki_apnic_member_repository')
replace_apnic = time.time()
os.system('rsync -a --delete rsync://rpki.apnic.net/repository/ ./RPKI_code/rpki_apnic_'+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+'')
os.system('rsync -a --delete rsync://rpki.apnic.net/member_repository ./RPKI_code/rpki_apnic_member_repository_'+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+'')
empty_apnic = time.time()
os.system('rsync -a --delete rsync://repository.lacnic.net/rpki ./RPKI_code/rpki_lacnic')
replace_lacnic = time.time()
os.system('rsync -a --delete rsync://repository.lacnic.net/rpki ./RPKI_code/rpki_lacnic_'+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+'')
empty_lacnic = time.time()
os.system('rsync -a --delete rsync://rpki.ripe.net/repository/ ./RPKI_code/rpki_ripe')
replace_ripe = time.time()
os.system('rsync -a --delete rsync://rpki.ripe.net/repository/ ./RPKI_code/rpki_ripe_'+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+'')
empty_ripe = time.time()
print('afrinic:' + str(replace_afrinic-begin) + ' ' + str(empty_afrinic-replace_afrinic))
print('arin:' + str(replace_arin-empty_afrinic) + ' ' + str(empty_arin-replace_arin))
print('apnic:' + str(replace_apnic-empty_arin) + ' ' + str(empty_apnic-replace_apnic))
print('lacnic:' + str(replace_lacnic-empty_apnic) + ' ' + str(empty_lacnic-replace_lacnic))
print('ripe:' + str(replace_ripe-empty_lacnic) + ' ' + str(empty_ripe-replace_ripe))