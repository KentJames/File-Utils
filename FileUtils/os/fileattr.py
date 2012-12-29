## Gets common attributes of file and stores them in a dict...

import sys
import os
from .. import exceptions

class fileattrException(exceptions.FileUtilsException):
    pass

class FileAttr(object):

    def __init__(self,filepath):

        self.filepath = filepath
        self.fileinfo = {}

        try:

            self.fileinfo.update({'FileSize': os.path.getsize(self.filepath)})
            self.fileinfo.update({'Exists':os.path.exists(self.filepath)})
            self.extension = os.path.splitext(self.filepath)[1]
            self.fileinfo.update({'Extension':self.extension})
        
        except OSError:
            
            raise fileattrException("os.fileattr.FileAttr.__init__")

        

    def __getitem__(self,key):

        return self.fileinfo[key]
