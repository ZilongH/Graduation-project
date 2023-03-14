# encoding = UTF-8
import asn1
import pyasn1.codec.der.decoder as decoder
import pyasn1_modules.rfc6482 as roa
import pyasn1_modules.rfc5652 as cms
import ipaddress
import typing

IPNetwork = typing.Union[ipaddress.IPv4Network, ipaddress.IPv6Network]
IPNetworkBits = typing.Tuple[int, int]
IPAddressFamily = {b'\x00\x01': 4, b'\x00\x02': 6}


def bitstring_to_net(bits: IPNetworkBits, version: int) -> IPNetwork:
    """Convert an ASN.1 BIT STRING representation to an IPNetwork."""
    len_map = {4: ipaddress.IPV4LENGTH, 6: ipaddress.IPV6LENGTH}
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


with open('98438B98677F11EA972EEA2EC4F9AE02.roa', 'rb') as f:
    data = f.read()

cms_content = decoder.decode(data, asn1Spec=cms.ContentInfo())
signed_data = decoder.decode(cms_content[0][1], asn1Spec=cms.SignedData())
roaContent = decoder.decode(signed_data[0]['encapContentInfo']['eContent'], asn1Spec=roa.RouteOriginAttestation())
# print(signed_data[0]['encapContentInfo']['eContent'])
# print(signed_data[1])
# print(cms_content[0][0]) # contentType
# print(cms_content[0][1]) # content

print(roaContent[0]['version'])
print(roaContent[0]['asID'])
###### ipAddrBlocks是一个List(在python中来说)，每个元素下是一个词典，每个元素对应一个IP类型(IPv4 or IPv6) ##
# ipv4
print(IPAddressFamily[bytes(roaContent[0]['ipAddrBlocks'][0]['addressFamily'])])
# print(int(roaContent[0]['ipAddrBlocks'][0]['addressFamily']))
for i in roaContent[0]['ipAddrBlocks'][0]['addresses']:  # roaContent[0]['ipAddrBlocks'][1]['addresses'] ipv6
    # print(i['address'])
    print(bitstring_to_net((bitstring_to_int(i['address']), len(i['address'])),
                           IPAddressFamily[bytes(roaContent[0]['ipAddrBlocks'][0]['addressFamily'])]))
    # print(i['address'].hex)
    # print(ipaddress.IPv4Address(i['address']))
    print(i['maxLength'])
# ipv6
print(IPAddressFamily[bytes(roaContent[0]['ipAddrBlocks'][1]['addressFamily'])])
for i in roaContent[0]['ipAddrBlocks'][1]['addresses']:
    print(bitstring_to_net((bitstring_to_int(i['address']), len(i['address'])),
                           IPAddressFamily[bytes(roaContent[0]['ipAddrBlocks'][1]['addressFamily'])]))
    # print(i['address'].hex)
    # print(ipaddress.IPv4Address(i['address']))
    print(i['maxLength'])
