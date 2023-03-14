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

file_dir = "../rpki"
dir_list = os.listdir(file_dir)
print(dir_list)
for i in dir_list:
    if '.cer' in i: # ripe
        print(i)
        file = file_dir + '/' + i
        # cert1 = RpkiCertificate(file)
        cert = crypto.load_certificate(crypto.FILETYPE_ASN1, open(file, 'rb').read())
        # print(str(cert.get_extension(5)).split('\n')[0].split('/')[4])
        dir = str(cert.get_extension(5)).split('\n')[0].split('/')[4]
        # sub = cert.get_extension(5)
        # print(type(sub))
        # print(cert1.getExtension()[5])
        # dir_list = os.listdir(file_dir + '/' + dir)
        # for j in dir_list: # aca
        #     if '.cer' in j:
        #         print(j)
        #         file = file_dir + '/' + dir + '/' + j
        #         cert = crypto.load_certificate(crypto.FILETYPE_ASN1, open(file, 'rb').read())
        #         print(str(cert.get_extension(5)).split('\n')[0].split('/')[4])
        #         dir = str(cert.get_extension(5)).split('\n')[0].split('/')[4]
        #         print(dir)
        #         dir_list = os.listdir(file_dir + '/' + dir)
        #         # print(dir_list)
        #         for k in dir_list: # DEFAULT
        #             if '.cer' in k:
        #                 file = file_dir + '/' + dir + '/' + k
        #                 cert = crypto.load_certificate(crypto.FILETYPE_ASN1, open(file, 'rb').read())
        #                 dir1 = str(cert.get_extension(5)).split('\n')[0].split(':')[1] + ':' + str(cert.get_extension(5)).split('\n')[0].split(':')[2] 
        #                 # print(str(cert.get_extension(5)).split('\n')[0].split(':')[1] + ':' + str(cert.get_extension(5)).split('\n')[0].split(':')[2])
        #                 len1 = len(dir1.split('/'))
        #                 if len1 < 8:
        #                     pass
        #                 else:
        #                     dir2 = file_dir + '/' + dir + '/' + dir1.split('/')[len1-4] + '/' + dir1.split('/')[len1-3] + '/' + dir1.split('/')[len1-2]
        #                     dir_list1 = os.listdir(dir2)
        #                 for l in dir_list1:
        #                     if '.roa' in l:
        #                         # print(l)
        #                         with open(dir2 + '/' + l, 'rb') as f:
        #                             data = f.read()
        #                         cms_content = decoder.decode(data, asn1Spec=cms.ContentInfo())
        #                         signed_data = decoder.decode(cms_content[0][1], asn1Spec=cms.SignedData())
        #                         roaContent = decoder.decode(signed_data[0]['encapContentInfo']['eContent'], asn1Spec=roa.RouteOriginAttestation())
                                
        #                         len_version = len(roaContent[0]['ipAddrBlocks'])
        #                         for m in range(len_version):
        #                             print(IPAddressFamily[bytes(roaContent[0]['ipAddrBlocks'][m]['addressFamily'])])
        #                             for n in roaContent[0]['ipAddrBlocks'][m]['addresses']:  # roaContent[0]['ipAddrBlocks'][1]['addresses'] ipv6
        #                                 # print(i['address'])
        #                                 print(bitstring_to_net((bitstring_to_int(n['address']), len(n['address'])),
        #                                                     IPAddressFamily[bytes(roaContent[0]['ipAddrBlocks'][m]['addressFamily'])]))
        #                                 # print(i['address'].hex)
        #                                 # print(ipaddress.IPv4Address(i['address']))
        #                                 print(n['maxLength'])