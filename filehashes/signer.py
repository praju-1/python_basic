#!/usr/bin/env python3

import hashlib
import zlib

class Signature(object):
    """
    A class represent a signature of file
    ...
    Attributes
    ----------
    algo = str
        algo of the signature

    Methods
    -------
    md5sum(filename):
        Return the md5 of file
    crc(filename):
        Return the crc value of file
    checksum(filename):
        Check the algo of signature, md5 or crc
    get_sign_algo():
        Get the algo of sign
    set_sign_algo(algo):
        Set the algo of sign
    """
    def __init__(self, algo):
        """
        Constructs all the necessary attributes for the Signature object.
        """
        self._algo = algo
    
    def md5sum(self, filename):
        m = hashlib.md5()
        for data in open(filename, "rb"):
            m.update(data)
        # hexdigest returns a HEX string representing the hash.
        return m.hexdigest()
    
    def crc(self, filename):
        crcvalue = 0
        with open(filename, 'rb') as afile:
            info = afile.read()
            while len(info) > 0:
                crcvalue = zlib.crc32(info, crcvalue)
                info = afile.read()

        return format(crcvalue & 0xFFFFFFFF, '08x')

    def checksum(self, filename):
        if self._algo == "md5":
            return self.md5sum(filename)
        return self.crc(filename)
    
    def get_sign_algo(self):
        return self._algo

    def set_sign_algo(self, algo):
        self._algo = algo
