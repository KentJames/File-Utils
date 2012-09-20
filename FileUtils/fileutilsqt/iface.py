import sys
from PyQt4 import QtCore,QtGui
from . import qtiface
from ..hashob import hashob

class StartQT4(QtGui.QMainWindow):

    def __init__(self,parent=None):


        QtGui.QWidget.__init__(self, parent)
        self.filename = None
        self.checksum = None
        self.string = None
        self.ui = qtiface.Ui_QTIface()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.FileSearch,QtCore.SIGNAL("clicked()"), self.file_browser)
        QtCore.QObject.connect(self.ui.checksumactivate,QtCore.SIGNAL("clicked()"), self.checksum_activate)


    def file_browser(self):
        fd = QtGui.QFileDialog(self)
        self.filename = fd.getOpenFileName()
        
    def checksum_activate(self):
        try:
            self.checksum = hashob.hasher_if(self.filename,'md5')
            self.outputtotextbox('Hashing file...')
            self.checksum.fileaccess()
        except hashob.FilePathException():
            pass
        
        self.checksum.hashtype()

        try:
            self.checksum.hashfile()
            self.outputtotextbox("Hash Type: {}".format(self.checksum.checksumtype))
            self.outputtotextbox("Hash: {}".format(self.checksum.returnhexhash()))
        except AttributeError:
            self.outputtotextbox("Ooops... Looks like an invalid or empty filepath was specified.")
            
            
##NOTE TO SELF: FIX EXCEPTIONS
       
        
    def outputtotextbox(self,string='None'):

        
        self.string = string
        self.ui.textEdit.append(self.string)







def main():
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())





if __name__=="__main__":
    main()
        

    
