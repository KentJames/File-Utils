#!/usr/bin/python



import sys
import os
from PyQt4 import QtCore,QtGui
from . import qtiface
from ..hashob import hashob

class StartQT4(QtGui.QMainWindow):

    def __init__(self,parent=None):


        QtGui.QWidget.__init__(self, parent)
        self.filename = None
        self.checksum = None
        self.hashtypeqt = None
        self.string = None
        self.ui = qtiface.Ui_QTIface()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.FileSearch,QtCore.SIGNAL("clicked()"), self.file_browser)
        QtCore.QObject.connect(self.ui.checksumactivate,QtCore.SIGNAL("clicked()"), self.checksum_activate)
        QtCore.QObject.connect(self.ui.cleartextboxbutton,QtCore.SIGNAL("clicked()"),self.clearall)
        QtCore.QObject.connect(self.ui.checksumtypeselection,QtCore.SIGNAL("activated(QString)"),self.sethashtype)
        QtCore.QObject.connect(self.ui.actionQuit_3,QtCore.SIGNAL("triggered()"),self.exitqt)
        QtCore.QObject.connect(self.ui.actionSave_hash_as,QtCore.SIGNAL("triggered()"),self.saveas)
        QtCore.QObject.connect(self.ui.actionHelp,QtCore.SIGNAL("triggered()"),self.showhelp)
        QtCore.QObject.connect(self.ui.actionAbout,QtCore.SIGNAL("triggered()"),self.showabout)
        self.sethashtype()

    def file_browser(self):

        fd = QtGui.QFileDialog(self)
        self.filename = fd.getOpenFileName()

        if self.filename is '':

            self.outputtotextbox("Null filepath...")

        else:
            
            self.outputtotextbox("File Path: {}".format(self.filename))
            if int( self.getfilesize()) > 1073741824:
                self.outputtotextbox("Warning: Your operating system states your file is very large.")
                self.outputtotextbox("Depending upon your hardware configuration, this file could take from several seconds to several minutes to hash.")
            else:
                pass
            self.outputtotextbox("Click Checksum to hash file...")
            self.outputtotextbox(" ")
            


    def getfilesize(self):

        return os.path.getsize(self.filename)


        
    
    def sethashtype(self):

        self.hashtypeqt = self.ui.checksumtypeselection.currentText()
        
        
        
    def checksum_activate(self):

        

        try:
            self.checksum = hashob.hasher_if(self.filename,self.hashtypeqt)
#            self.outputtotextbox('Hashing file...')
            self.checksum.fileaccess()
            self.checksum.hashtype()
            self.checksum.hashfile()
            self.outputtotextbox("File: {}".format(self.checksum.returnfilename()))
            self.outputtotextbox("File Size: {} bytes".format(self.checksum.returnfilesize()))
            self.outputtotextbox("Hash Type: {}".format(self.checksum.returnchecksumtype()))
            self.outputtotextbox("Hash: {}".format(self.checksum.returnhexhash()))
            self.outputtotextbox(" ")
                

        except hashob.FilePathException:
            self.outputtotextbox("Empty filepath specified...")
        except hashob.HashTypeException:
            self.outputtotextbox("Invalid hash type specified...")
        except AttributeError:
            self.outputtotextbox("Ooops...Looks like an unexpected error occured!")



       
        
    def outputtotextbox(self,string='None'):

        
        self.string = string
        self.ui.textEdit.append(self.string)


    def clearall(self):

        self.ui.textEdit.setText("")
        self.filename = None

    def saveas(self):
        pass

    def showhelp(self):
        pass
    
    def showabout(self):
        pass


    def exitqt(self):

        sys.exit(QtGui.QApplication.exec_())




def main():
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
        

    
