from ftplib import FTP
import os
import sys
import datetime
import pymysql
# rsync -r rsync://rpki.ripe.net/repository ./rpki

def ftp_connect(host, username, password):
    ftp = FTP()
    ftp.set_debuglevel(0)
    ftp.connect(host, 21)
    ftp.login(username, password)
    # ftp.set_pasv(False)
    return ftp

def downloadfile(ftp, path, repo, k):
    bufsize = 1024
    fp = open('roas_'+str(datetime.date.today())+'_'+repo[k]+'.txt', 'wb')
    ftp.retrbinary('RETR ' + path, fp.write, bufsize)
    ftp.set_debuglevel(0)

if __name__ == "__main__":
    repo = ['afrinic', 'apnic', 'arin', 'lacnic', 'ripencc']
    ftp = ftp_connect("ftp.ripe.net", "", "")
    db = pymysql.connect(host="localhost", user="ken", passwd="123456", database='rpki', charset='utf8')
    cursor = db.cursor()
    for k in range(5):
        # ftp = ftp_connect("ftp.ripe.net", "", "")
        downloadfile(ftp, "/rpki/"+repo[k]+".tal/"+str(datetime.date.today().year)+"/"+str('{:02d}'.format(datetime.date.today().month))+"/"+str('{:02d}'.format(datetime.date.today().day))+"/roas.csv", repo, k)
        sql_createtable = "create table "+repo[k]+"_"+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+" (URI varchar(200), ASN varchar(30), IP_pre varchar(50), Max_len varchar(10), Not_Before varchar(50), Not_After varchar(50));"
        cursor.execute(sql_createtable)
        fq = open('roas_'+str(datetime.date.today())+'_'+repo[k]+'.txt', encoding='utf-8')
        for i in fq.readlines()[1:]:
            # print(i)
            j = len(i.split(','))
            # print(i.split(',')[j])
            sql_insert = "insert into "+repo[k]+"_"+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+"(URI, ASN, IP_pre, Max_len, Not_Before, Not_After) values('"+i.split(',')[j-6]+"', '"+i.split(',')[j-5]+"', '"+i.split(',')[j-4]+"', '"+i.split(',')[j-3]+"', '"+i.split(',')[j-2]+"', '"+i.split(',')[j-1].split('\n')[0]+"');"
            # print(sql_insert)
            cursor.execute(sql_insert)
            cursor.connection.commit()
    ftp.close()
    # downloadfile(ftp, "/rpki/afrinic.tal/"+str(datetime.date.today().year)+"/"+str('{:02d}'.format(datetime.date.today().month))+"/"+str('{:02d}'.format(datetime.date.today().day))+"/roas.csv")
    # db = pymysql.connect(host="localhost", user="ken", passwd="123456", database='rpki', charset='utf8')
    # cursor = db.cursor()
    # sql_createtable = "create table afrinic_"+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+" (URI varchar(200), ASN varchar(10), IP_pre varchar(20), Max_len varchar(10), Not_Before varchar(50), Not_After varchar(50));"
    # cursor.execute(sql_createtable)
    # fq = open('roas_'+str(datetime.date.today())+'.txt', encoding='utf-8')
    # for i in fq.readlines()[1:]:
    #     print(i)
    #     j = len(i.split(','))
    #     # print(i.split(',')[j])
    #     sql_insert = "insert into afrinic_"+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+"(URI, ASN, IP_pre, Max_len, Not_Before, Not_After) values('"+i.split(',')[j-6]+"', '"+i.split(',')[j-5]+"', '"+i.split(',')[j-4]+"', '"+i.split(',')[j-3]+"', '"+i.split(',')[j-2]+"', '"+i.split(',')[j-1].split('\n')[0]+"');"
    #     print(sql_insert)
    #     cursor.execute(sql_insert)
    #     cursor.connection.commit()