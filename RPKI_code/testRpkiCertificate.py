#coding:utf-8

from RpkiCertificate import RpkiCertificate


def testVerify():
	file_dir = "ripe-ncc-ta.cer"
	cert = RpkiCertificate(file_dir)
	#print(cert.getSignature())
	#print(SHA256())
	#result = cert.verify(cert.getCertificateCrypto())
	#assert True == result

testVerify()
