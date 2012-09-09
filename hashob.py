## !/usr/bin/python
## Simple file hashing. Can be used as imported objects or standalone
## terminal hash.
##
## James Kent 2012
##

import hashlib
import argparse
import sys


class hasher():

    def __init__(self):
        
        self.filename = None
        self.file = None
        self.check = None
        self.block = None

        
    def openfile(self):

        # Open file to be hashed in binary mode.

        try:
           
            self.file = open(self.filename,'rb')

        except IOError as msg:

            print(msg)
            sys.exit(1)

        




    def hashfile(self):

        for self.block in iter(lambda: self.file.read(32768),b""):

            self.check.update(self.block)
            

    def asciihash(self):

        return self.check.digest()
    

    def hexhash(self):

        return self.check.hexdigest()
    

class hasher_cli(hasher):

    def __init__(self):
        
        hasher.__init__(self)
        self.args = None
        self.command = None
        
    def parse_commandline(self):

        self.command = argparse.ArgumentParser(description=
                                               'Checksum Tool v1.1.1')
        self.command.add_argument('type',metavar = 'C', default = 'md5',
                             help = ('Specifies type of checksum. md5,'
                                     ' sha1, sha224, sha256, sha384'
                                     ' and sha512 supported.'))
        self.command.add_argument('file',metavar = 'F',
                             help = 'File to Checksum')
        self.args = self.command.parse_args()
        self.hashtype()
        self.fileaccess()

    def hashtype(self):

        try:
            
            self.check = getattr(hashlib, self.args.type)()

        except AttributeError as msg:

            print(msg)
            print(
"""Incorrect hash type used.
Use -h or --help to identify correct hash types.""")
            sys.exit(1)

        


    def fileaccess(self):

        self.filename = self.args.file
        self.openfile()
        






    
        
def main():
    
    hashobject = hasher_cli()
    hashobject.parse_commandline()
    hashobject.hashfile()
    print("Hash: {}".format(hashobject.hexhash()))



if __name__=="__main__":
    main()
        
