##!/usr/bin/python3


# Used as an interface for python crytographic hash functions.
#


from .. import exceptions
import hashlib
import argparse
import sys
import os


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


#Base object for hasher. 
class hasher(object):

    def __init__(self):
        
        self.filename = None
        self.file = None
        self.checksumtype = None
        self.check = None
        self.block = None
        self.hashsums = {}
        
       
        
    def openfile(self):

        # Open file to be hashed in binary mode. If filepath(self.filename) is None or does not
        # exist, then throw an error to be caught externally.

        try:
           
            self.file = open(self.filename,'rb')

        except IOError as msg:

            raise FilePathException("hasher.openfile")

        except TypeError:
            
            raise FilePathException("hasher.openfile")
            

        
    def hashfile(self):

        # Read and digest files...

        self.readfile()
        self.digestfiles()

    def readfile(self):

        # Read file opened in self.file and scan through reading 32768 bytes at a time until
        # no more data is encountered.
        
        for self.block in iter(lambda: self.file.read(32768),b""):

            #Update the hash algorithm with the bytes we have read

            self.check.update(self.block)


        

    def digestfiles(self):

        #Digest hash algorithm output and store in a dictionary.

        self.hashsums.update({'asciikey':self.check.digest()})
        self.hashsums.update({'hexkey':self.check.hexdigest()})        

    def returnhexhash(self):

        return self.hashsums['hexkey']

    def returnasciihash(self):

        return self.hashsums['asciikey']


    def returnfilename(self):
        
        return self.filename

    def returnfilesize(self):

        return os.path.getsize(self.filename)

    def returnchecksumtype(self):

        return self.checksumtype
        
    

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
        if self.filepath is '' or None:
            raise FilePathException("hasher_if.filepath")
        self.checksumtype = checksumtype
        if self.checksumtype is '' or None:
            raise HashTypeException("hasher_if.hashtype")

    def fileaccess(self):
        self.filename = self.filepath
        self.openfile()

    def hashtype(self):

        #Try and instantiate object with parameter specified in init constructor, if init
        #constructor is invalid, then throw an exception to be caught externally.

        try:
            self.check = getattr(hashlib,self.checksumtype)()

        except AttributeError as msg:
            raise HashTypeException("hashif.hashtype")
            
        
    
            

