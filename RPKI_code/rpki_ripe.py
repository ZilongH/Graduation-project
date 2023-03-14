from RpkiCertificate import RpkiCertificate
from OpenSSL import crypto
import sys
import os
import asn1
import pyasn1.codec.der.decoder as decoder
import pyasn1_modules.rfc6482 as roa
import pyasn1_modules.rfc5652 as cms
import ipaddress
import typing
import pymysql
import datetime
import time

IPNetwork = typing.Union[ipaddress.IPv4Network, ipaddress.IPv6Network]
IPNetworkBits = typing.Tuple[int, int]
IPAddressFamily = {b'\x00\x01': 'IPv4', b'\x00\x02': 'IPv6'}


def bitstring_to_net(bits: IPNetworkBits, version: int) -> IPNetwork:
    """Convert an ASN.1 BIT STRING representation to an IPNetwork."""
    len_map = {'IPv4': ipaddress.IPV4LENGTH, 'IPv6': ipaddress.IPV6LENGTH}
    value, netbits = bits
    hostbits = len_map[version] - netbits
    net = ipaddress.ip_network((value << hostbits, netbits))
    return typing.cast(IPNetwork, net)


def bitstring_to_int(bits):
    num = len(bits)
    value = 0
    for elem in range(num):
        value = value * 2 + (bits[elem])
    return value

# rsync -r rsync://rpki.afrinic.net/repository ./RPKI_code/rpki_afrinic
# rsync -r rsymc://rpki.arin.net/repository ./RPKI_code/rpki_arin
# rsync -r rsync://rpki.ripe.net/repository ./RPKI_code/rpki_ripe
# rsync -r rsync://repository.lacnic.net/rpki ./RPKI_code/rpki_lacnic
# rsync -r rsync://rpki.apnic.net/repository ./RPKI_code/rpki_apnic
begin = time.time()
os.system('rsync -a --delete rsync://rpki.ripe.net/repository/ ./RPKI_code/rpki_ripe_'+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+'')
rsync = time.time()
db = pymysql.connect(host="localhost", user="ken", passwd="123456", database='rpki', charset='utf8')
cursor = db.cursor()
sql_createtable = "create table certificate_ripe_"+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+" (Cert_name varchar(100), Cert_URI varchar(200) primary key, Auth_URI varchar(200), Sub_URI varchar(200), Content longtext, id varchar(20));"
cursor.execute(sql_createtable)
sql_createtable = "create table roa_ripe_"+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+" (ROA_name varchar(100), ROA_URI varchar(200) primary key, Cert_URI varchar(200), Content longtext, id varchar(20), foreign key(Cert_URI) references certificate_ripe_"+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+"(Cert_URI));"
cursor.execute(sql_createtable)
sql_createtable = "create table asn_ip_ripe_"+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+" (ASN varchar(10), IP_block varchar(50), version varchar(5), max_length varchar(5), ROA_URI varchar(200), id varchar(20), foreign key (ROA_URI) references roa_ripe_"+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+"(ROA_URI));"
cursor.execute(sql_createtable)
file_dir = "RPKI_code/rpki_ripe_"+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+""
dir_list = os.listdir(file_dir)
# print(dir_list)
param_1 = []
for i in dir_list:
    if '.cer' in i: # ripe
        # print(i)
        file = file_dir + '/' + i
        # cert1 = RpkiCertificate(file)
        cert = crypto.load_certificate(crypto.FILETYPE_ASN1, open(file, 'rb').read())
        os.system('openssl x509 -inform DER -in '+file+' -text > 1.txt')
        f = open('1.txt', 'r')
        content = f.read()
        # print(str(cert.get_extension(5)).split('\n')[0].split('/')[4])
        dir = str(cert.get_extension(5)).split('\n')[0].split('/')[4]
        auth = str(cert.get_extension(4)).split(':')[1] + ':' + str(cert.get_extension(4)).split(':')[2] # aca
        sub = str(cert.get_extension(5)).split('\n')[0].split(':')[1] + ':' + str(cert.get_extension(5)).split('\n')[0].split(':')[2]
        # print(cert1.getExtension()[5])
        url = 'rsync://rpki.ripe.net/repository/'
        param_certificate = (i, url+i, auth, sub, content, '0')
        param_1.append(param_certificate)
        # print(param)
        # print(param_1)
        # sql_insert = "insert into certificate_"+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+" values('"+i+"', '"+(url+i)+"', '"+auth+"', '"+sub+"', '"+content+"');"
        # print(sql_insert)
        # cursor.execute(sql_insert)
        # cursor.connection.commit()
        f.close()
        dir_list1 = os.listdir(file_dir + '/' + dir)
        for j in dir_list1: # aca
            if '.cer' in j:
                # print(j)
                # print(dir)
                file = file_dir + '/' + dir + '/' + j
                cert = crypto.load_certificate(crypto.FILETYPE_ASN1, open(file, 'rb').read())
                os.system('openssl x509 -inform DER -in '+file+' -text > 1.txt')
                f = open('1.txt', 'r')
                content = f.read()
                auth = str(cert.get_extension(4)).split(':')[1] + ':' + str(cert.get_extension(4)).split(':')[2]
                sub = str(cert.get_extension(5)).split('\n')[0].split(':')[1] + ':' + str(cert.get_extension(5)).split('\n')[0].split(':')[2]
                # print(str(cert.get_extension(5)).split('\n')[0].split('/')[4])
                dir1 = str(cert.get_extension(5)).split('\n')[0].split('/')[4] # DEFAULT
                # print(dir)
                dir_list2 = os.listdir(file_dir + '/' + dir1)
                # print(dir_list)
                # sql_insert = "insert into certificate_"+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+" values('"+j+"', '"+(url + dir + '/' + j)+"', '"+auth+"', '"+sub+"', '"+content+"');"
                param_certificate = (j, url + dir + '/' + j, auth, sub, content, '0')
                param_1.append(param_certificate)
                # cursor.execute(sql_insert)
                # cursor.connection.commit()
                f.close()
                param_2 = []
                param_3 = []
                param_4 = []
                for k in dir_list2: # DEFAULT
                    if '.cer' in k:
                        file = file_dir + '/' + dir1 + '/' + k
                        # print(file)
                        cert = crypto.load_certificate(crypto.FILETYPE_ASN1, open(file, 'rb').read())
                        os.system('openssl x509 -inform DER -in '+file+' -text > 1.txt')
                        f = open('1.txt', 'r')
                        content = f.read()
                        auth = str(cert.get_extension(4)).split(':')[1] + ':' + str(cert.get_extension(4)).split(':')[2]
                        sub = str(cert.get_extension(5)).split('\n')[0].split(':')[1] + ':' + str(cert.get_extension(5)).split('\n')[0].split(':')[2]
                        dir2 = str(cert.get_extension(5)).split('\n')[0].split(':')[1] + ':' + str(cert.get_extension(5)).split('\n')[0].split(':')[2] 
                        # print(str(cert.get_extension(5)).split('\n')[0].split(':')[1] + ':' + str(cert.get_extension(5)).split('\n')[0].split(':')[2])
                        # sql_insert = "insert into certificate_"+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+" values('"+k+"', '"+(url + dir1 + '/' + k)+"', '"+auth+"', '"+sub+"', '"+content+"');"
                        param_certificate = (k, url + dir1 + '/' + k, auth, sub, content, '0')
                        param_1.append(param_certificate)
                        # cursor.execute(sql_insert)
                        # cursor.connection.commit()
                        f.close()
                        len1 = len(dir2.split('/'))
                        if len1 < 8:
                            continue
                        else:
                            dir3 = file_dir + '/' + dir1 + '/' + dir2.split('/')[len1-4] + '/' + dir2.split('/')[len1-3] + '/' + dir2.split('/')[len1-2]
                            dir_list3 = os.listdir(dir3)
                        for l in dir_list3:
                            if '.roa' in l:
                                # print(l)
                                # print(count)
                                with open(dir3 + '/' + l, 'rb') as f:
                                    data = f.read()
                                cms_content = decoder.decode(data, asn1Spec=cms.ContentInfo())
                                signed_data = decoder.decode(cms_content[0][1], asn1Spec=cms.SignedData())
                                roaContent = decoder.decode(signed_data[0]['encapContentInfo']['eContent'], asn1Spec=roa.RouteOriginAttestation())
                                # print(roaContent[0])
                                dir4 = url + dir1 + '/' + dir2.split('/')[len1-4] + '/' + dir2.split('/')[len1-3] + '/' + dir2.split('/')[len1-2] + '/' + l
                                # print(url + dir1 + '/' + k)
                                # sql_insert1 = "insert into roa_"+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+" values('"+l+"', '"+dir4+"', '"+(url + dir1 + '/' + k)+"', '"+str(roaContent[0])+"');"
                                param_roa = (l, dir4, url + dir1 + '/' + k, str(roaContent[0]), '0')
                                param_2.append(param_roa)
                                # cursor.execute(sql_insert1)
                                len_version = len(roaContent[0]['ipAddrBlocks'])
                                for m in range(len_version):
                                    # print(IPAddressFamily[bytes(roaContent[0]['ipAddrBlocks'][m]['addressFamily'])])
                                    for n in roaContent[0]['ipAddrBlocks'][m]['addresses']:  # roaContent[0]['ipAddrBlocks'][1]['addresses'] ipv6
                                        print(bitstring_to_net((bitstring_to_int(n['address']), len(n['address'])),
                                                            IPAddressFamily[bytes(roaContent[0]['ipAddrBlocks'][m]['addressFamily'])]))
                                        # print(n['maxLength'])
                                        IP_block = bitstring_to_net((bitstring_to_int(n['address']), len(n['address'])),
                                                            IPAddressFamily[bytes(roaContent[0]['ipAddrBlocks'][m]['addressFamily'])])
                                        # sql_insert2 = "insert into asn_ip_"+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+" values('"+str(roaContent[0]['asID'])+"', '"+str(IP_block)+"', '"+IPAddressFamily[bytes(roaContent[0]['ipAddrBlocks'][m]['addressFamily'])]+"', '"+str(n['maxLength'])+"', '"+dir4+"');"
                                        param_ai = (str(roaContent[0]['asID']), str(IP_block), IPAddressFamily[bytes(roaContent[0]['ipAddrBlocks'][m]['addressFamily'])], str(n['maxLength']), dir4, '0')
                                        param_3.append(param_ai)
mysql = time.time()
try:
    sql_1 = "insert into certificate_ripe_"+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+" values(%s, %s, %s, %s, %s, %s);"
    cursor.executemany(sql_1, param_1)
except Exception as e:
    print("MySQL: %s error: %s" %(sql_1, e))
finally:
    cursor.connection.commit()
try:
    sql_2 = "insert into roa_ripe_"+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+" values(%s, %s, %s, %s, %s);"
    cursor.executemany(sql_2, param_2)
except Exception as e:
    print("MySQL: %s error: %s" %(sql_2, e))
finally:
    cursor.connection.commit()
try:
    sql_3 = "insert into asn_ip_ripe_"+str(datetime.date.today().year)+"_"+str('{:02d}'.format(datetime.date.today().month))+"_"+str('{:02d}'.format(datetime.date.today().day))+" values(%s, %s, %s, %s, %s, %s);"
    cursor.executemany(sql_3, param_3)
except Exception as e:
    print("MySQL: %s error: %s" %(sql_3, e))
finally:
    cursor.connection.commit()
cursor.close()
db.close()
end = time.time()
print(begin, rsync, mysql, end)