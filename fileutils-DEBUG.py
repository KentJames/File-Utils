#!/usr/bin/python3

#Run this as main from command line to spawn the main HashUtils application.
#NOTE: You MUST have the pyqt framework installed or this will not work.

import sys
from FileUtils.fileutilsqt import iface



def main():
    app = iface.QtGui.QApplication(sys.argv)
    myapp = iface.StartQT4()
    myapp.show()
    sys.exit(app.exec_())
    

if __name__=="__main__":
    main()
