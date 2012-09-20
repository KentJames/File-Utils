
## Simple file hashing. Can be used as imported objects or standalone
## terminal hash.
##
## James Kent 2012
##


from .. import exceptions
import hashlib
import argparse
import sys


class hashexception(exceptions.FileUtilsException):
    pass

class FilePathException(hashexception):
    pass

class HashTypeException(hashexception):
    pass

class HashDataException(hashexception):
    pass
        

##Acts as an interface with which to hash files and stores hashes
##in a dictionary.

class hasher():

    def __init__(self):
        
        self.filename = None
        self.file = None
        self.check = None
        self.block = None
        self.hashsums = {}
       
        
    def openfile(self):

        # Open file to be hashed in binary mode.

        try:
           
            self.file = open(self.filename,'rb')

        except IOError as msg:

            print(msg)
            

        
    def hashfile(self):


        self.readfile()


        
        


        self.digestfiles()

    def readfile(self):

        for self.block in iter(lambda: self.file.read(32768),b""):

            self.check.update(self.block)
        

    def digestfiles(self):

        self.hashsums.update({'asciikey':self.check.digest()})
        self.hashsums.update({'hexkey':self.check.hexdigest()})        

    def returnhexhash(self):

        return self.hashsums['hexkey']

    def returnasciihash(self):

        return self.hashsums['asciikey']
        
    

##Class used for acting as a standalone command line hashing file.

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
            

    def fileaccess(self):

        self.filename = self.args.file
        self.openfile()
        

class hasher_if(hasher):

    def __init__(self,filepath,checksumtype):
        hasher.__init__(self)
        self.filepath = filepath
        if self.filepath is None:
            raise FilePathException("hasher_if.filepath")
        self.checksumtype = checksumtype
        if self.checksumtype is None:
            raise HashTypeException("hasher_if.hashtype")

    def fileaccess(self):
        self.filename = self.filepath
        self.openfile()

    def hashtype(self):

        try:
            self.check = getattr(hashlib,self.checksumtype)()

        except AttributeError as msg:
            raise HashTypeException("hashif.hashtype")
            return(msg)
        
    
            
        




    
        
def main():
    
    hashobject = hasher_cli()
    hashobject.parse_commandline()
    hashobject.hashfile()

    print("Hash: {}".format(hashobject.returnhexhash()))



if __name__=="__main__":
    main()
        
