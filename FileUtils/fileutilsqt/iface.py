#!/usr/bin/python3
#
#  Spawns main form for HashUtils, and manages events and child forms.
#
#  To do: 
#  Cleanup module package dependencies
#  Formatting of ascii/utf output
#  Finish Dialog Connections
#  Implement saveas feature for specific hash types.
#  Open specific hash types to verify
#  Implement table instead of textedit.
#
#
#  Made by: James Kent (jameschristopherkent@gmail.com)
#  Source is hosted here: https://github.com/KentJames/File-Utils
#
#  Copyright (C) 2013  James Kent (jameschristopherkent@gmail.com)
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#
#



import sys
import os

from PyQt4 import QtCore,QtGui
from ..os import platformdetect,fileattr
from ..hashob import hashob
from .Forms import aboutdialog,qtiface
from ..import exceptions

class PyQTException(exceptions.FileUtilsException):
    pass

class StartQT4(QtGui.QMainWindow):

    def __init__(self,parent=None):

        # Initialise widgets

        QtGui.QWidget.__init__(self, parent)
        QtCore.QThread.__init__(self)

        # Setup Variables

        self.systeminfo = platformdetect.detectos()
        self.filename = None
        self.verifyfilename = None
        self.savehashfilename = None
        self.checksum = None
        self.hashtypeqt = None
        self.string = None
        self.lastknownhash = None

        self.fileattributes = None
        self.verifyfileattributes = None

        
        ## Setup Main UI form

        self.ui = qtiface.Ui_QTIface()
        self.ui.setupUi(self)

        

        ## Connect all buttons to event functions.

        # Pushbuttons
        QtCore.QObject.connect(self.ui.FileSearch,QtCore.SIGNAL("clicked()"), self.file_browser)
        QtCore.QObject.connect(self.ui.checksumactivate,QtCore.SIGNAL("clicked()"), self.checksum_activate)
        QtCore.QObject.connect(self.ui.cleartextboxbutton,QtCore.SIGNAL("clicked()"),self.clearall)
        
        QtCore.QObject.connect(self.ui.verifyfilebrowserbutton,QtCore.SIGNAL("clicked()"),self.file_browser_verify)
        QtCore.QObject.connect(self.ui.Verifybutton,QtCore.SIGNAL("clicked()"),self.comparehashvalues)

        #Combobuttons

        QtCore.QObject.connect(self.ui.checksumtypeselection,QtCore.SIGNAL("activated(QString)"),self.sethashtype)


        #Menus
        QtCore.QObject.connect(self.ui.actionQuit_3,QtCore.SIGNAL("triggered()"),self.exitqt)
        QtCore.QObject.connect(self.ui.actionSave_hash_as,QtCore.SIGNAL("triggered()"),self.saveas)
        QtCore.QObject.connect(self.ui.actionHelp,QtCore.SIGNAL("triggered()"),self.showhelp)
        QtCore.QObject.connect(self.ui.actionAbout,QtCore.SIGNAL("triggered()"),self.showabout)

        #Establish default hash
        self.sethashtype()






    def file_browser(self):

        fd = QtGui.QFileDialog(self)
        self.filename = fd.getOpenFileName()
        self.fileattributes = fileattr.FileAttr(self.filename)

        if self.filename is '':

            self.outputtotextbox("Null filepath...")

        else:
            
            self.outputtotextbox("File Path: {}".format(self.filename))
            if int( self.fileattributes['FileSize']) > 1073741824:
                self.outputtotextbox("Warning: Your operating system states your file is very large.")
                self.outputtotextbox("Depending upon your hardware configuration, this file could take from several seconds to several minutes to hash.")
            else:
                pass
            self.outputtotextbox("Click Checksum to hash file...")
            self.outputtotextbox(" ")


            
    def file_browser_verify(self):

        fd = QtGui.QFileDialog(self)
        self.verifyfilename = fd.getOpenFileName()
        self.verifyfileattributes = fileattr.FileAttr(self.filename)

##
##    def getfilesize(self):
##
##        return os.path.getsize(self.filename)
##
##
        
    
    def sethashtype(self):

        self.hashtypeqt = self.ui.checksumtypeselection.currentText()
        
        
        
    def checksum_activate(self):

        


        self.checksum = HashWorker(self.filename,self.hashtypeqt)
        self.checksum.asciihash.connect(self.giveupthehashbro)

        self.checksum.start()


    def giveupthehashbro(self, val):

        self.lastknownhash = val
        self.outputtotextbox("File: {}".format(self.filename))
        self.outputtotextbox("File Size: {} bytes".format(self.fileattributes['FileSize']))
        self.outputtotextbox("Hash Type: {}".format(self.hashtypeqt))
        self.outputtotextbox("Hash: {}".format(self.lastknownhash))
        self.outputtotextbox(" ")

    def comparehashvalues(self):

        
        if self.lastknownhash==self.ui.verifylineedit.text():
            self.ui.verifylineedit.setText("Verification PASSED!")
        else:
            self.ui.verifylineedit.setText("Verification FAILED!")        

    

       
        
    def outputtotextbox(self,string='None'):

        
        self.string = string
        self.ui.textEdit.append(self.string)


    def clearall(self):

        self.ui.textEdit.setText("")
        self.filename = None

    def saveas(self):
        
        fd = QtGui.QFileDialog(self)
        self.savehashfilename = fd.getSaveFileName()

    def showhelp(self):
        pass
    
    def showabout(self):

        
        
        Dialog = QtGui.QDialog()

        self.aboutdialog = aboutdialog.Ui_Dialog()
        self.aboutdialog.setupUi(Dialog)
        self.aboutdialog.label.setText(QtGui.QApplication.translate("Dialog", """HashUtil v0.8.0

Created by James Kent

Source: https://github.com/KentJames/File-Utils""", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutdialog.label_2.setText(QtGui.QApplication.translate("Dialog", """System Info: 

Platform: {} {} 

Version: {}""".format(self.systeminfo['OS'],self.systeminfo['Release'],self.systeminfo['Version'])))
        Dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        Dialog.exec_()
        

    def exitqt(self):

        
        sys.exit(QtGui.QApplication.exit())

class HashWorker(QtCore.QThread):

    def __init__(self,filename,hashtype,parent=None):
        
        QtCore.QThread.__init__(self)

        self.filename = filename
        self.hashtype = hashtype

        self.hashobject = None
        self.resulthash = None

    def __del__(self):
        self.wait()

    def run(self):

        self.HashExecute()
        self.returnHash()
        

    def HashExecute(self):

       
        self.hashobject = hashob.hasher_if(self.filename,self.hashtype)
        
        self.hashobject.fileaccess()
        self.hashobject.hashtype()
        self.hashobject.hashfile()


        
        
        self.resulthash = self.hashobject.returnhexhash()

    # Connect signal, this serves as communication of the file hash back to the main thread.

    asciihash = QtCore.pyqtSignal(str)


    def returnHash(self):

        self.asciihash.emit(self.resulthash)
        self.quit()






def main():
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
        

    
