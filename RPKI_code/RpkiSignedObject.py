#coding: utf-8
from pyasn1_modules import rfc3852
from pyasn1_modules import rfc4055
from pyasn1_modules import rfc5280
from pyasn1_modules import rfc5652
from pyasn1_modules import rfc6482
from pyasn1_modules import rfc6486
from pyasn1.codec.der.decoder import decode
from pyasn1.codec.der.encoder import encode
#from pyasn1.type import univ
from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.hashes import SHA256
import hashlib

class RpkiSignedObject():
    def __init__(self, file_dir):
        if isinstance(file_dir, str):
            with open(file_dir, "rb") as rfile:
                content = rfile.read()
            self.file_bytes = content
        else:
            self.file_bytes = bytes()
        self.bytesToFormat(file_dir)

    def bytesToFormat(self, file_dir):
        self.signedObject, _ = decode(self.file_bytes, asn1Spec = rfc5652.ContentInfo(), decodeOpenTypes = True)
        oid = self.signedObject['content']['encapContentInfo']['eContentType']
        substrate = self.signedObject['content']['encapContentInfo']['eContent']
        self.eContent, _ = decode(substrate, asn1Spec = rfc5652.cmsContentTypesMap[oid], decodeOpenTypes = True)
        self.eeCertificate = self.signedObject['content']['certificates'][0]['certificate']
        self.eeCertificateCrypto = x509.load_der_x509_certificate(encode(self.eeCertificate))

    def getEeCertificate(self):
        return encode(self.eeCertificate)
    
    def getEeCertificateCrypto(self):
        return self.eeCertificateCrypto

    def getSignature(self):
        return encode(self.signedObject['content']['signerInfos'][0]['signature'])
        #signature =  self.signedObject['content']['signerInfos'][0]['signature']._value
        #signature =  self.signedObject['content']['signerInfos'][0]['signature'].asOctets()
        #return signature

    def getSignatureAlgorithm(self):
        return self.signedObject['content']['signerInfos'][0]['signatureAlgorithm']['algorithm']

    def getEContent(self):
        return self.signedObject['content']['encapContentInfo']['eContent']
        #return encode(self.signedObject['content']['encapContentInfo'])

    def getDigest(self):
        for i in self.signedObject['content']['signerInfos']:
            for j in i['signedAttrs']:
                if j['attrType'] == rfc5652.id_messageDigest:
                    return j['attrValues'][0].asOctets()

    def generateDigest(self):
        hash_fun = hashlib.sha256()
        hash_fun.update(self.getEContent().asOctets())
        return hash_fun.digest()

    def verify(self, parent_cert):    
        try:
            for i in self.signedObject['content']['signerInfos']:
                if i['signatureAlgorithm']['algorithm'] == rfc4055.sha256WithRSAEncryption:
                    parent_cert.public_key().verify(self.getSignature(), self.getDigest(), padding.PKCS1v15(), SHA256())
                return True
            else:
                return 123
        except:
            return False

        '''
        try:
            if self.getSignatureAlgorithm() == rfc4055.sha256WithRSAEncryption:
                parent_cert.public_key().verify(self.getSignature(), self.getEContent(), padding.PKCS1v15(), SHA256())
                return True
            else:
                return 123
            #return False
        except:
            return False
        '''
        '''
        if self.getSignatureAlgorithm() == rfc4055.sha256WithRSAEncryption:
            parent_cert.public_key().verify(self.getSignature(), self.getEContent(), padding.PKCS1v15(), SHA256())
            return True
        else:
            return False
        '''
            
    def __str__(self):
    	return self.signedObject.__str__()
