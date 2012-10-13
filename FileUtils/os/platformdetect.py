#Module used to quickly collate information about platform in use and store in a dictionary
#
# James Kent, jameschristopherkent@gmail.com

import platform
from .. import exceptions

class platformexception(exceptions.FileUtilsException):
    pass 

class detectos(object):

    def __init__(self):
        
        self.infodict = {}
        self.detectplatform()
        
    def __getitem__(self,key):

        return self.infodict[key]


    def detectplatform(self):

        self.infodict.update({'OS':platform.system()})
        self.infodict.update({'Release':platform.release()})
        self.infodict.update({'Version':platform.version()})
    #    self.returndata()


    #def returndata(self):

     #   return self.infodict


        
