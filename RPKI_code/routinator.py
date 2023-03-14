from ftplib import FTP
import os
import sys
import datetime
import pymysql

def ftp_connect(host, username, password):
    ftp = FTP()
    ftp.set_debuglevel(0)
    ftp.connect(host, 21)
    ftp.login(username, password)
    return ftp

def downloadfile(ftp, path, repo, k):
    bufsize = 1024
    fp = open('./RPKI_ftp/routinator_'+str(datetime.date.today())+'_'+repo[k]+'.txt', 'wb')
    ftp.retrbinary('RETR ' + path, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

if __name__ == "__main__":
    repo = ['afrinic', 'apnic', 'arin', 'lacnic', 'ripencc']
    ftp = ftp_connect("ftp.ripe.net", "", "")
    for k in range(5):
        downloadfile(ftp, "/rpki/"+repo[k]+".tal/"+str(datetime.date.today().year)+"/"+str('{:02d}'.format(datetime.date.today().month))+"/"+str('{:02d}'.format(datetime.date.today().day))+"/routinator.log", repo, k)
    ftp.close()