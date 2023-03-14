# coding: utf-8
from pyasn1_modules import rfc5280
from pyasn1_modules import rfc6487
from pyasn1_modules import rfc2315
from pyasn1.codec.der.decoder import decode
from pyasn1.codec.der.encoder import encode
#from pyasn1.type import univ
from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import padding


class RpkiCertificate():
    def __init__(self, file_dir):
        if isinstance(file_dir, str):
            with open(file_dir, "rb") as rfile:
                content = rfile.read()
            self.file_bytes = content
        else:
            self.file_bytes = bytes()
        self.bytesToFormat()

    def bytesToFormat(self):
        self.cert_asn1, _ = decode(self.file_bytes, asn1Spec=rfc5280.Certificate())
        self.cert_crypto = x509.load_der_x509_certificate(self.file_bytes)

    def getCertificateCrypto(self):
        return self.cert_crypto

    def getTbsCertificate(self):
        return encode(self.cert_asn1['tbsCertificate'])

    def getSubject(self):
        return self.cert_asn1['tbsCertificate']['subject']

    def getIssuer(self):
        return encode(self.cert_asn1['tbsCertificate']['issuer'])

    def getExtension(self):
        return encode(self.cert_asn1['tbsCertificate']['extensions'])

    def isRoot(self):
        return self.getSubject() == self.getIssuer()

    def getSubjectPublicKeyInfo(self):
        return encode(self.cert_asn1['tbsCertificate']['subjectPublicKeyInfo'])

    def getSignature(self):
        signature = self.cert_asn1['signature'].asOctets()
        return signature

    def getCertificateBytes(self):
        return self.file_bytes

    def getSignatureAlgorithm(self):
        return self.cert_asn1["signatureAlgorithm"]["algorithm"]

    def verify(self, parent_cert):
        try:
            #parent_cert.public_key().verify(self.cert_crypto.signature, self.cert_crypto.tbs_certificate_bytes, padding.PKCS1v15(), self.cert_crypto.signature_hash_algorithm)
            #parent_cert.public_key().verify(self.cert_crypto.signature, self.getTbsCertificate(), padding.PKCS1v15(), self.cert_crypto.signature_hash_algorithm)
            parent_cert.public_key().verify(self.getSignature(), self.getTbsCertificate(), padding.PKCS1v15(), self.cert_crypto.signature_hash_algorithm)
            return True
        except:
            return False

    def __str__(self):
        return self.cert_asn1.__str__()

        
