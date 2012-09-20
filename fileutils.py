#!/usr/bin/python3

import sys
from FileUtils.hashob import hashob
from FileUtils.fileutilsqt import iface



def main():
    app = iface.QtGui.QApplication(sys.argv)
    myapp = iface.StartQT4()
    myapp.show()
    sys.exit(app.exec_())
    

if __name__=="__main__":
    main()
